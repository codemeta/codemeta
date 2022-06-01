# Crosswalk for Citation File Format 1.2.0

## Format information

Citation File Format (CFF) is a YAML format for providing citation metdaata for software (and experimentally for datasets).

- Website: <https://citation-file-format.github.io/>
- Specifications: <https://github.com/citation-file-format/citation-file-format/blob/1.2.0/schema-guide.md>
- Schema: <https://github.com/citation-file-format/citation-file-format/blob/1.2.0/schema.json> (JSON Schema)

## Crosswalk specifics

The following sections provide details for directional mapping 
in cases where mapping is not bidirectionally unambiguous.

### `downloadUrl` <=> different potential mapping targets

- CodeMeta `downloadUrl`: "If the file can be downloaded, URL to download the binary." As per <https://github.com/codemeta/codemeta/pull/263/files#r763105765>, it signifies a URL pointing to a single binary (or archive) for download.

#### CFF to CodeMeta

In some cases, values for the following CFF fields could also be mappable to CodeMeta `downloadUrl`:

- `repository-artifact`, when the URL points directly to a downloadable artifact
- `url`, when the URL points directly to a downloadable artifact
- `repository`, when the URL points directly to a downloadable artifact
- `identifiers[i].type==url`, when the identifier resolves directly to a downloadable artifact

Future versions of CFF may document this more clearly (<https://github.com/citation-file-format/citation-file-format/issues/326>).

### `installUrl` <=> different potential mapping targets (not crosswalked)

#### CodeMeta to CFF

CodeMeta `installUrl` may map to `url`.
However, as `url` is a generic URL field ("The URL of a landing page/website for the software or dataset."), some semantics will be lost when mapping this way.

#### CFF to CodeMeta

In some cases, the following CFF fields may be mappable to `installURL`:

- `url`, when the URL points to a URL where the software is installed
- `repository`, when the repository provides an installed artifact of the software
- `identifiers[i].type==url`, when the resolved URL is to an installed artifact of the software

### `softwareRequirements`/`softwareSuggestions` <=> `references`

- CodeMeta `softwareRequirements`: "Required software dependencies"
- CodeMeta `softwareSuggestions`: "Optional dependencies , e.g. for optional features, code development, etc"
- CFF `references`: "Reference(s) to other creative works."

#### CodeMeta to CFF

The scope of `references` could be documented more clearly in CFF (<https://github.com/citation-file-format/citation-file-format/issues/327>).
CFF's `references` is meant to work like a references list for a paper, 
e.g., should include prior work that the work builds on.
Required dependencies are interpreted to clearly constitute prior work that software builds on.
Therefore, everything that is in `softwareRequirements` should go into `references`, but not the other way round.

Optional dependencies and dependencies needed for code development could be assumed 
to build on the software (i.e., require prior existence of the software).
Therefore, the software would constitute a `reference` *from* the `softwareSuggestion`,
but not the other way round.
I.e., `softwareSuggestions` should *not* be included in `references`.

#### CFF to CodeMeta

Not all CFF `references` can be assumed to be `softwareRequirements`,
as `references` can contain arbitrary other work that the software builds on.
The same is true for `softwareSuggestions`.
`references` therefore should not be included automatically in either, 
without further manual verification.

### `author` <=> `authors`

CFF `authors` is an array of CFF `person` or CFF `entity` objects.

### `citation` <=> `preferred-citation`/`references`/CFF root document

- CodeMeta `citation`: "A citation or reference to another creative work, such as another publication, web page, scholarly article, etc."
- CFF `preferred-citation`: "A reference to another work that should be cited instead of the software or dataset itself."
- CFF `references`: "Reference(s) to other creative works."

#### CodeMeta to CFF

- When the `citation` is a citation to another work describing the software (a "meta" work, e.g., a software paper in JOSS, a traditional paper about the software), it maps to CFF `preferred-citation`.
- When the `citation` is to a work not describing the software itself, it maps to an entry in CFF `references`

#### CFF to CodeMeta

CFF `preferred-citation` maps to CodeMeta `citation`.
Any given entry in CFF `references` may map to CodeMeta `citation`, given the latter's definition as "A citation or reference to another creative work, such as another publication, web page, scholarly article, etc."

### `license` <=> `license`/`license-url`

#### CodeMeta to CFF

If the CodeMeta `license` contains an SPDX identifier (or its URL) that is recognized in CFF to be a valid value of CFF `license` (list [here](https://github.com/citation-file-format/citation-file-format/blob/1.2.0/schema.json#L516-L978)),
it maps to `license`.
If the CodeMeta `license` contains a URL to a license unrecognized in CFF, it maps to `license-url`.
If the CodeMeta `license` contains a `schema:CreativeWork`, which contains a URL to the license, it maps to `license-url`.
`schema:CreativeWork`s without URLs to the license cannot be mapped.

#### CFF to CodeMeta

CFF `license-url` maps to CodeMeta `license`.
CFF `license` maps to CodeMeta `license` following the pattern `https://spdx.org/licenses/<value of CFF license>.html`.
In analogy, any and all items in a given list of licenses that CFF `license` accepts maps to CodeMeta `license`.

### `version`/`softwareVersion` <=> `version`

#### CodeMeta to CFF

Both CodeMeta `version` and CodeMeta `softwareVersion` map to CFF `version` (in the root of the `CITATION.cff` file).
CodeMeta is ambiguous for this term (see <https://github.com/codemeta/codemeta/issues/264>), and it is unclear which value of the terms should be mapped if they differ.

#### CFF to CodeMeta

CFF `version` maps to both CodeMeta `version` and CodeMeta `software Version`.
CodeMeta is ambiguous for this term (see <https://github.com/codemeta/codemeta/issues/264>).
Until this is resolved, CFF `version` should probably be mapped to both.

### `isPartOf`/`hasPart` <=> `identifiers`

CFF doesn't (yet, see  <https://github.com/citation-file-format/citation-file-format/issues/69#issuecomment-904546233>) support these qualifiers for `identifiers` in a machine-readable way.
`identifiers` is a list of identifiers pertaining to the software ("The identifiers of the software or dataset.").

As of version 1.2.0, CFF `identifiers` may have an `identifier.description`, which may specify the relation of the identifier to another object (but only in human-readable form),
and which may be mapped to either `isPartOf` or `hasPart`.

#### CodeMeta to CFF

If the `schema:CreativeWork` for CodeMeta `isPartOf` or `hasPart` contain an identifier or definitive URL, 
these map to a CFF `identifier`.
The target type of the CFF `identifier` could be heuristically determined based on the identifier in the CodeMeta value.
The qualifying part `hasPart` and `isPartOf` can be encoded (automatically) in CFF `identifier.description` in plain text.

#### CFF to CodeMeta

Values in CFF `identifiers` map to either CodeMeta `hasPart` or CodeMeta `isPartOf`, 
if the respective relationship can be determined from the CFF `identifier.description`, either manually or heuristically.

### `identifier` <=> `identifiers`/`person.orcid`/`doi`

Mapping depends on how a CodeMeta instance uses the term, which is ambiguously documented ("URL identifer, ideally an ORCID ID for individuals, a FundRef ID for funders").

#### CodeMeta to CFF

If the CodeMeta `identifier` is an identifier for the described software, it maps to CFF `identifiers`.
If the CodeMeta `identifier` is a DOI for the described software, it maps to either CFF `doi` or a CFF `identifier` of CFF `identifier.type` `doi`.
If the CodeMeta `identifier` is the identifier for a person (e.g., an author), and is an ORCID id, it maps to CFF `person.orcid`.

#### CFF to CodeMeta

CFF `person.orcid` maps to CodeMeta `identifier` of the respective person.
Any single CFF `identifier` maps to `identifier`.
The respective CFF `identifier` to use for an n:1 mapping needs to be determined manually or heuristically from the list of available CFF `identifiers`.
A CFF `doi` maps to `identifier`.

### `sameAs` <=> `identifiers.url / url`

#### CodeMeta to CFF

CodeMeta `sameAs` URL maps to a CFF `identifiers.url`

#### CFF to CodeMeta

Any given CFF `identifiers.url` maps to CodeMeta `sameAs`.
CFF `url` may map to CodeMeta `sameAs` if the URL qualifies for such use.

### `url` <=> `url` (and potentially others)

The general case is that CodeMeta `url` maps to CFF `url` and vice versa.

#### CodeMeta to CFF

Depending on what the CodeMeta `url` points to, it may be mapped to one of CFF `repository`, `repository-code`, `repository-artifact` or `identifiers[i].type==url`
if this mapping provides better semantics than mapping to CFF `url`.

#### CFF to CodeMeta

If no better suited option to map to CodeMeta `url` is available, CFF `repository` can map to CodeMeta `url`.

### `relatedLink` <=> `url` (and potentially others)

The general case is that CodeMeta `relatedLink` maps to CFF `url` and vice versa.

#### CodeMeta to CFF

Depending on what the CodeMeta `relatedLink` points to, it may be mapped to one of CFF `repository`, `repository-code`, `repository-artifact` or `identifiers[i].type==url`
if this mapping provides better semantics than mapping to CFF `url`.

#### CFF to CodeMeta

If no better suited option to map to CodeMeta `relatedLink` is available, CFF `repository` can map to CodeMeta `relatedLink`.

### `type` <=> `type`

#### CodeMeta to CFF

If CodeMeta `type` is `https://schema.org/SoftwareApplication` or `https://schema.org/SoftwareSourceCode`, it maps to CFF `type: software`.
If CodeMeta `type` is `https://schema.org/Dataset`, it maps to CFF `type: dataset`.

#### CFF to CodeMeta

CFF `type: software` maps to CodeMeta `type` with a value of `https://schema.org/SoftwareApplication` or `https://schema.org/SoftwareSourceCode`.
CFF `type: dataset` maps to CodeMeta `type` with a value of `https://schema.org/Dataset`.

### `id` <=> `identifiers` / `doi`

Mapping depends on the target of the CodeMeta `id`.

#### CodeMeta to CFF

If the CodeMeta `id` is the URL for a DOI resolver for the software DOI, it maps to CFF `doi` and CFF `identifiers` of type `doi`.
If the CodeMeta `id` is a Software Heritage ID or a URL resolving that ID, it maps to CFF `identifiers` of type `swh`.
If the CodeMeta `id` is any other URL, it maps to CFF `identifiers` of type `url`.
If the CodeMeta `id` is a string used to refer to the node eslewhere in the same document, it maps to CFF `identifiers` of type `other`.

#### CFF to CodeMeta

Any one of the objects in CFF `identifiers` maps to CodeMeta `id`.
CFF `doi` maps to CodeMeta `id`.