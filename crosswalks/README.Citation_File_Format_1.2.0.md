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

