## Minimal metadata for code: a crosswalk

At the [Open Science Codefest](http://nceas.github.io/open-science-codefest/), we met to discuss the metadata for scientific software. Participants included:

- Abigail Cabunoc / @abbycabs
- Matt Jones / @metamattj
- Carly Strasser / @carlystrasser
- Corinna Gries / @CorinnaGries

The discussion centered around metadata for software to enable software discovery, software reuse and interpretation, and software citation. A number of existing software metadata efforts exist and have been in use for varying lengths of time.  These include:

- [eml-software](http://knb.ecoinformatics.org/sofwtare/eml)
- [code.jsonld](http://www.arfon.org/json-ld-for-software-discovery-reuse-and-credit)
- Figshare
- Zenodo
- [EBM Tools database](http://www.ebmtools.org/)
- [DataONE Software registry](https://www.dataone.org/software-tools)
- [Winning model documentation](https://www.kaggle.com/wiki/WinningModelDocumentationTemplate)
- [MyExperiment workflow repository](http://www.myexperiment.org/)


Table 1: Mapping of fields in use by various software metadata efforts

| Field                  | Figshare | Zenodo | code.jsonld | codemeta |
| ---------------------- | -------- | ------ | ----------- | -------- |
| Title                  | X        | X      | X           | X        |
| Identifier             | X        | X      | X           | X        |
| Author(s)              | X        | X      | X           | X        |
| - AuthorName           | X        | X      | X           | X        |
| - AuthorIdentifier     |          |        | X           | X        |
| - AuthorEmail          |          |        | X           | X        |
| - AuthorAffiliation    |          | X      |             | X        |
| UploadedBy             |          | X      |             | X        |
| ControlledTerm         |          |        |             | X        |
| - Category             | X        |        |             |          |
| - Collection           |          | X      |             |          |
| - Community            |          | X      |             |          |
| - ObjectType           | X        | X      |             | X        |
| Tag/Keyword            | X        | X      | X           | X        |
| Description            | X        | X      | X           | X        |
| RelatedLink            | X        | X      |             | X        |
| - CodeRepository       |          |        | X           | X        |
| - Readme               |          |        |             | X        |
| - BuildInstructions    |          |        |             | X        |
| - ContIntegration      |          |        |             | X        |
| - IssueTracker         |          |        |             | X        |
| AccessList             |          |        |             | X        |
| - PublicPrivate        | X        |        |             |          |
| - PublicEmbargoPrivate |          | X      |             |          |
| License                | X        | X      | X           | X        |
| PubDate                |          | X      |             | X        |
| - DateRetrieved        | X        |        |             |          |
| - DateCreated          |          |        | X           |          |
| Inputs                 |          |        |             | X        |
| Outputs                |          |        |             | X        |
| Function               |          |        |             | X        |
| Dependency             |          |        |             | X        |
| TestCoverage           |          |        |             | X        |
| DocsCoverage           |          |        |             | X        |
| IsAuthomatedBuild      |          |        |             | X        |
| Package                |          |        |             | X        |
| - ZippedCode           | X        | X      |             | X        |
| - FileSet              | X        |        |             |          |

 

- Other things to add:
    -  Annotations
        - attribute selected fields to someone
    	- Zenodo, Figshare allow users to comment 



