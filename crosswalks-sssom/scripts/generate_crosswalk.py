import csv
import json
import os
import sys
from pathlib import Path

from sssom.parsers import parse_sssom_table
from sssom.writers import write_owl

header = [
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "match_type",
    "confidence",
]


# Get the prefix of a concept
def get_prefix(concept, context):
    if concept in context:
        mapping = context[concept]
        if isinstance(mapping, dict):
            id_value = mapping.get("@id")
            if id_value and ":" in id_value:
                prefix = id_value.split(":")[0]
                return prefix
    return "codemeta"


# Function to convert a csv to a tsv and turtle
def convert_csv_to_tsv(
    input_metadata_file, input_file, output_file, ttl_file, context_data
):
    input_metadata_f = open(input_metadata_file, mode="r", newline="", encoding="utf-8")
    reader_metadata = csv.reader(input_metadata_f)
    # Skip the first line
    next(reader_metadata)

    # Open the input CSV file for reading
    input_f = open(input_file, mode="r", newline="", encoding="utf-8")
    # reader = csv.reader(input_f)
    reader = csv.DictReader(input_f)

    # Open the output TSV file for writing
    output_f = open(output_file, mode="w", newline="", encoding="utf-8")

    for row in reader_metadata:
        # Join the row with tabs and comment it
        commented_row = "# " + "\t".join(row) + "\n"
        output_f.write(commented_row)
    # writer.writerows(commented_lines)
    writer = csv.writer(output_f, delimiter="\t")
    writer.writerow(header)

    # Write each row from CSV to TSV
    for row in reader:
        type_relation = row["type_relation"]
        source_term = row["source_term"]

        if type_relation == "exact_match":
            predicate_id = "skos:exactMatch"
        elif type_relation == "part_of":
            predicate_id = "skos:closeMatch"
        elif type_relation == "more_specific_than":
            predicate_id = "skos:narrower"
        elif type_relation == "more_generic_than":
            predicate_id = "skos:broader"
        elif type_relation == "close_match":
            predicate_id = "skos:closeMatch"
        else:
            if source_term and type_relation != "":
                print(
                    f"Error: Skipping row {row} with invalid relation type {type_relation}"
                )
            continue

        row = [
            "subject:" + source_term,
            source_term,
            predicate_id,
            get_prefix(source_term, context_data) + ":" + source_term,
            source_term,
            "SSSOM:HumanCurated",
            1,
        ]
        writer.writerow(row)

    # Close the files
    input_f.close()
    input_metadata_f.close()
    output_f.close()

    msdf = parse_sssom_table(output_tsv_file)

    with open(ttl_file, "w") as f:
        write_owl(msdf, f)


# Example usage
if len(sys.argv) != 3:
    print("Error: This script requires exactly two arguments.")
    print("Usage: python script.py <metadata_file.yml> <input_file.csv>")
    sys.exit(1)  # Exit with an error code
metadata_file = Path(sys.argv[1])
input_file = Path(sys.argv[2])

if not metadata_file.is_file():
    print(f"Error: Metadata file {metadata_file} does not exist.")
    sys.exit(1)  # Exit with an error code
if not os.path.isfile(input_file):
    print(f"Error: Input file {input_file} does not exist.")
    sys.exit(1)  # Exit with an error code

target_vocab = metadata_file.name.split("-")[0]
output_dir = input_file.absolute().parent / f"{target_vocab}-sssom-outputs"
if not output_dir.exists():
    output_dir.mkdir(parents=True, exist_ok=True)

output_tsv_file = output_dir / input_file.with_suffix(".sssom.tsv").name
output_ttl_file = output_dir / input_file.with_suffix(".sssom.ttl").name

this_dir = Path(__file__).parent.resolve()
codemeta_jsonld_file = this_dir / ".." / ".." / "codemeta.jsonld"

# Load codemeta.jsonld JSON-LD file with the mapping of the concepts to schema.org or codemeta
with open(codemeta_jsonld_file, encoding="utf-8") as f:
    jsonld_data = json.load(f)
context_data = jsonld_data.get("@context", {})

convert_csv_to_tsv(
    sys.argv[1], sys.argv[2], output_tsv_file, output_ttl_file, context_data
)
