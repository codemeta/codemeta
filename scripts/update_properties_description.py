#!/usr/bin/env python3
"""Keeps properties_description.csv in sync with the current CodeMeta terms.

Sources:

* codemeta.jsonld: its @context says which properties are current.
* codemeta_all.jsonld: definitions (type, description) of the codemeta: terms.
* schema.org release: only used to look up schema: terms that are in the
  context but not yet in the CSV. It is downloaded on demand (the version is
  read from codemeta.jsonld); use --schema-org to give a local file or URL.

What it does:

* removes the rows of properties that are no longer in the context;
* refreshes Type and Description of the codemeta: rows from codemeta_all.jsonld
  (cosmetic differences, like a trailing full stop, are ignored);
* adds a row for every current property that is missing, after the last row
  with the same Parent Type;
* leaves all the other (hand-curated) schema: rows untouched.

Usage:

    python scripts/update_properties_description.py          # rewrite the CSV
    python scripts/update_properties_description.py --check  # exit 1 if out of sync
"""

import argparse
import csv
import json
import re
import sys
import urllib.request
from pathlib import Path


REPO_DIR = Path(__file__).parent.parent

CONTEXT_PATH = REPO_DIR / "codemeta.jsonld"
ALL_PATH = REPO_DIR / "codemeta_all.jsonld"
PROP_DESC_PATH = REPO_DIR / "properties_description.csv"

SCHEMA_ORG_URL = (
    "https://raw.githubusercontent.com/schemaorg/schemaorg/main/"
    "data/releases/{version}/schemaorg-current-https.jsonld"
)

FIELDS = ["Parent Type", "Property", "Type", "Description"]


def load_json(source):
    """Loads JSON from a local path or from an http(s) URL."""
    if str(source).startswith(("http://", "https://")):
        with urllib.request.urlopen(str(source), timeout=60) as response:
            return json.load(response)
    with open(source, encoding="utf-8") as fd:
        return json.load(fd)


def ids(value):
    """Ids of a JSON-LD value that is a reference or a list of references."""
    if value is None:
        return []
    if not isinstance(value, list):
        value = [value]
    return [v["@id"] if isinstance(v, dict) else v for v in value]


def local_name(identifier):
    """'schema:URL' -> 'URL'."""
    return identifier.split(":", 1)[1]


def current_properties(context):
    """Maps each property name in the @context to its id (schema:... or
    codemeta:...). Types (capitalised names), keywords and prefix declarations
    are skipped."""
    properties = {}
    for name, value in context.items():
        target = value.get("@id", "") if isinstance(value, dict) else value
        if name[0].islower() and target.startswith(("schema:", "codemeta:")):
            properties[name] = target
    return properties


def range_text(node):
    """'Text or URL', from the ranges of a property."""
    return " or ".join(
        sorted(local_name(t) for t in ids(node.get("schema:rangeIncludes")))
    )


def clean_comment(text):
    """schema.org comments use [[Type]] and [text](url); the CSV has plain text."""
    text = re.sub(r"\[\[(\w+)\]\]", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return " ".join(text.split())


def codemeta_row(name, node):
    domains = {local_name(d) for d in ids(node.get("schema:domainIncludes"))}
    parent = (
        "codemeta:SoftwareSourceCode"
        if "SoftwareSourceCode" in domains
        else "codemeta:SoftwareApplication"
    )
    return {
        "Parent Type": parent,
        "Property": name,
        "Type": range_text(node),
        "Description": clean_comment(node["rdfs:comment"]),
    }


def schema_row(name, node, parents):
    """Parent Type is the first of the types already used in the CSV that
    the property applies to."""
    domains = ids(node.get("schema:domainIncludes"))
    parent = next((p for p in parents if p in domains), None)
    if parent is None:
        raise SystemExit(
            f"Cannot place {name}: its domains {domains} do not include any "
            f"Parent Type used in the CSV. Add the row by hand."
        )
    return {
        "Parent Type": parent,
        "Property": name,
        "Type": range_text(node),
        "Description": clean_comment(node["rdfs:comment"]),
    }


def same_description(a, b):
    return a.strip().rstrip(".") == b.strip().rstrip(".")


def same_type(a, b):
    return set(a.split(" or ")) == set(b.split(" or "))


def insert_row(rows, new):
    """Inserts the row after the last one with the same Parent Type."""
    last = max(
        (i for i, r in enumerate(rows) if r["Parent Type"] == new["Parent Type"]),
        default=len(rows) - 1,
    )
    rows.insert(last + 1, new)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not write anything; exit with 1 if the CSV is out of sync",
    )
    parser.add_argument(
        "--schema-org",
        metavar="FILE_OR_URL",
        help="schema.org JSON-LD release to use instead of downloading it",
    )
    args = parser.parse_args()

    context = load_json(CONTEXT_PATH)
    properties = current_properties(context["@context"])
    definitions = {n["@id"]: n for n in load_json(ALL_PATH)["@graph"]}

    with open(PROP_DESC_PATH, encoding="utf-8", newline="") as fd:
        old_rows = list(csv.DictReader(fd))

    schema_graph = {}

    def schema_node(target):
        if not schema_graph:
            version = re.search(
                r"v(\d+\.\d+)", context["@graph"][0]["schema:schemaVersion"]
            ).group(1)
            source = args.schema_org or SCHEMA_ORG_URL.format(version=version)
            graph = load_json(source)["@graph"]
            schema_graph.update({n["@id"]: n for n in graph})
        return schema_graph[target]

    changes = []
    rows = []

    # 1. Remove retired properties, refresh the codemeta: rows.
    for row in old_rows:
        name = row["Property"]
        if name not in properties:
            changes.append(f"removed {name} ({row['Parent Type']})")
            continue
        node = definitions.get(f"codemeta:{name}")
        if row["Parent Type"].startswith("codemeta:") and node is not None:
            new = codemeta_row(name, node)
            if new["Parent Type"] != row["Parent Type"]:
                changes.append(
                    f"updated {name}: Parent Type "
                    f"{row['Parent Type']} -> {new['Parent Type']}"
                )
                row["Parent Type"] = new["Parent Type"]
            if not same_type(row["Type"], new["Type"]):
                changes.append(
                    f"updated {name}: Type {row['Type']!r} -> {new['Type']!r}"
                )
                row["Type"] = new["Type"]
            if not same_description(row["Description"], new["Description"]):
                changes.append(f"updated {name}: Description")
                row["Description"] = new["Description"]
        rows.append(row)

    # 2. Add current properties that are missing.
    parents = list(
        dict.fromkeys(
            r["Parent Type"] for r in rows if r["Parent Type"].startswith("schema:")
        )
    )
    present = {r["Property"] for r in rows}
    for name, target in properties.items():
        if name in present:
            continue
        if target.startswith("codemeta:"):
            if target not in definitions:
                raise SystemExit(f"{target} is in the context but not in {ALL_PATH.name}")
            new = codemeta_row(name, definitions[target])
        else:
            new = schema_row(name, schema_node(target), parents)
        insert_row(rows, new)
        changes.append(f"added {name} ({new['Parent Type']}, {new['Type']})")

    if not changes:
        print("properties_description.csv is up to date.")
        return 0

    print("\n".join(changes))
    if args.check:
        print("\nproperties_description.csv is out of sync.", file=sys.stderr)
        return 1

    with open(PROP_DESC_PATH, "w", encoding="utf-8", newline="") as fd:
        writer = csv.DictWriter(fd, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nWrote {PROP_DESC_PATH.name}. Review the added rows: Parent Type and "
          f"Type are inferred for schema: terms.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
