# Crosswalk for Citation File Format 1.2.0

## Format information

Citation File Format (CFF) is a YAML format for providing citation metdaata for software (and experimentally for datasets).

- Website: <https://citation-file-format.github.io/>
- Specifications: <https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md>
- Schema: <https://github.com/citation-file-format/citation-file-format/blob/main/schema.json> (JSON Schema)

## Crosswalk specifics

### `downloadUrl` <=> `repository-artifact`

- CodeMeta `downloadUrl`: "If the file can be downloaded, URL to download the binary."
- CFF `repository-artifact`: "The URL of the work in a build artifact/binary repository."

While the scope of `repository-artifact` is documented to be somewhat narrower than `downloadUrl`, 
its main use case is discovery (e.g. for reuse and reproducibility),
which is arguably the same as for `downloadUrl`.
Therefore the two can be assumed to signify the same.

Future versions of CFF may document this more clearly (https://github.com/citation-file-format/citation-file-format/issues/326).

### `softwareRequirements`/`softwareSuggestions` <=> `references`

- CodeMeta `softwareRequirements`: "Required software dependencies"
- CodeMeta `softwareSuggestions`: "Optional dependencies , e.g. for optional features, code development, etc"
- CFF `references`: "Reference(s) to other creative works."

#### CodeMeta to CFF

The scope of `references` could be documented more clearly in CFF (https://github.com/citation-file-format/citation-file-format/issues/327).
CFF's `references` is meant to work like a references list for a paper, 
e.g., should include prior work that the work builds on.
Required dependencies are interpreted to clearly constitute prior work that software builds on.
Therefore, everything that is in `softwareRequirements` should go into `references`.

Optional dependencies and dependencies needed for code development could be assumed 
to build on the software (i.e., require prior existence of the software).
Therefore, the software would constitute a `reference` *from* the `softwareSuggestion`,
but not the other way round.
I.e., `softwareSuggestions` should *not* be included in `references`.

#### CFF to CodeMeta

Not all CFF `references` can be assumed to be `softwareRequirements`,
as `references` can contain arbitrary other work that the software builds on.
The same is even more clearly true for `softwareSuggestions`.
`references` therefore should not be included automatically in either, 
without further manual verification.

### `author` <=> `authors`

CFF `authors` is an array of CFF `person` or CFF `entity` objects.

### `citation` <=> `preferred-citation`/`references`/CFF root document

- CodeMeta `citation`: "A citation or reference to another creative work, such as another publication, web page, scholarly article, etc."
- CFF `preferred-citation`: "A reference to another work that should be cited instead of the software or dataset itself."
- CFF `references`: "Reference(s) to other creative works."
- CFF root document: The citation metadata for the software (or dataset) that the `CITATION.cff` file pertains to

#### CodeMeta to CFF

Understanding `citation` in CodeMeta to be the citation for the described software, the relationships are as follows:

- When the `citation` is a citation of the software itself, it maps to the citation metadata provided in the root of a `CITATION.cff` file.
- When the `citation` is a citation to another work describing the software (a "meta" work, e.g., a software paper in JOSS, a traditional paper about the software), it maps to CFF `preferred-citation`.
- Diverging from the understanding of `citation` being the citation to the software, when the `citation` is to an unrelated work, it maps to an entry in CFF `references`

#### CFF to CodeMeta

The citation metadata in the root of a `CITATION.cff` file maps to CodeMeta `citation`.

### `license` <=> `license`/`license-url`

#### CodeMeta to CFF

If the CodeMeta `license` contains an SPDX identifier (or its URL) that is recognized in CFF to be a valid value of CFF `license` (list [here](https://github.com/citation-file-format/citation-file-format/blob/main/schema.json#L516-L978)),
it maps to `license`.
If the CodeMeta `license` contains a URL to an license unrecognized in CFF, it maps to `license-url`.
If the CodeMeta `license` contains a `schema:CreativeWork`, which contains a URL to the license, it maps to `license-url`.
`schema:CreativeWork`s without URLs to the license cannot be mapped.

#### CFF to CodeMeta

CFF `license-url` maps to CodeMeta `license`.
CFF `license` maps to CodeMeta `license` following the pattern `https://spdx.org/licenses/<value of CFF license>.html`.

### `version`/`softwareVersion` <=> `version`

#### CodeMeta to CFF

Both CodeMeta `version` and CodeMeta `softwareVersion` map to CFF `version` (in the root of the `CITATION.cff` file).
CodeMeta is ambiguous for this term (see <https://github.com/codemeta/codemeta/issues/264>), and it is unclear which value of the terms should be mapped if they differ.

#### CFF to CodeMeta

CFF `version` maps to both CodeMeta `version` and CodeMeta `software Version`.
CodeMeta is ambiguous for this term (see <https://github.com/codemeta/codemeta/issues/264>).
Until this is resolved, CFF `version` should probably be mapped to both.

### `isPartOf`/`hasPart` <=> `identifiers`

CFF doesn't (yet? See  https://github.com/citation-file-format/citation-file-format/issues/69#issuecomment-904546233) support these qualifiers for `identifiers` in a machine-readable way.
`identifiers` is a list of identifiers pertaining to the software ("The identifiers of the software or dataset.").

#### CodeMeta to CFF

If the `schema:CreativeWork` for CodeMeta `isPartOf` or `hasPart` contain an identifier or definitive URL, 
these maps to a CFF `identifier`.
The target type of the CFF `identifier` could be heuristically determined based on the identifier in the CodeMeta value.
The qualifying part `hasPart` and `isPartOf` can be encoded (automatically) in CFF `identifier.description` in plain text.

#### CFF to CodeMeta

Values in CFF `identifiers` map to either CodeMeta `hasPart` or CodeMeta `isPartOf`, 
if the respective relationship can be determined from the CFF `identifier.description`, either manually or heuristically.

#### `identifier` <=> `identifiers`/`person.orcid`/`doi`

Mapping depends on how a CodeMeta instance uses the term, which is ambiguously documented ("URL identifer, ideally an ORCID ID for individuals, a FundRef ID for funders").

#### CodeMeta to CFF

If the CodeMeta `identifier` is an identifier for the described software, it maps to CFF `identifiers`.
If the CodeMeta `identifier` is a DOI for the described software, it maps to either CFF `doi` or a CFF `identifier` of CFF `identifier.type` `doi`.
If the CodeMeta `identifier` is the identifier for a person (e.g., an author), and is an ORCID id, it maps to CFF `person.orcid`.

#### CFF to CodeMeta

CFF `person.orcid` maps to CodeMeta `identifier` of the respective person.
A single CFF `identifier` maps to `identifier`.
The respective CFF `identifier` to use for the mapping needs to be determined manually or heuristically from the list of available CFF `identifiers`, 
e.g., if there is only one identifier, and no value for CFF `doi` is supplied, or if the single identifier is of `identifier.type` `doi` 
and has the same value as `doi` (but `doi` may override this behaviour, see next sentence).
A CFF `doi` maps to `identifier` and should be used even in the case where there additionally are CFF `identifiers`.





#### CodeMeta to CFF
#### CFF to CodeMeta



#### CodeMeta to CFF
#### CFF to CodeMeta



#### CodeMeta to CFF
#### CFF to CodeMeta



#### CodeMeta to CFF
#### CFF to CodeMeta



#### CodeMeta to CFF
#### CFF to CodeMeta


#### CodeMeta to CFF
#### CFF to CodeMeta