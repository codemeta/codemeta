The CodeMeta project has adopted a set of terms that represent concepts used to describe software. These concepts are common among the schemas used by prominent software source code and research data repositories,
citation services such as GitHub, figshare, Zenodo, and DataCite. These terms are not used to define a software metadata standard or ontology, but rather as a means to transfer software descriptions between users, repositories, software indexes, citation services and others.

The following is the list of concepts used by CodeMeta.

Each concept has a corresponding entry in the CodeMeta JSON-LD context file *codemeta.jsonld*, which is
used in the serialization of a software description to a CodeMeta instance file. The CodeMeta usage
of JSON-LD is described in more detail in the [CodeMeta Developer Guide](https://github.com/codemeta/codemeta/blob/master/developer-guide.md).

Note: Terms marked with ~~strikethough~~ were once considered by the CodeMeta team but have since been deemed
unneeded or inappropriate for CodeMeta software descriptions.

### ~~AccessList~~
The set of rules that specifying the user identities and their level of access (e.g. read, write, update) to the software.

Usage of this term has been discontinued because access control will have a repository specific
implementation and may not be transferrable to other repositories.

### Agent
A person or organization that has a role in designing, authoring, funding, maintaining or licensing the software. The type of agent is specified using a "Role".

Example agent types are "creator", "contributor", "funder".

JSON-LD context name: *agents*

### AgentId
A universally unique character string that is associated with the software agent.

JSON-LD context name: @id

### AgentAffiliation
The institution, organization or other group that the agent is associated with.

JSON-LD context name: *affiliation*

### AgentEmail
The email address associated with the agent of the software.

JSON-LD context name: *email*

### AgentName
The name of the institution, organization, individuals or other entities that had a role in the creation of the software.

JSON-LD context name: *name*

### BuildLink
A URL for the instructions to create an executable version of the software from source code.

JSON-LD context name: *buildInstructions*

### CILink
A URL for the continuous integration system used to build the software automatically after updates to the source code repository.

JSON-LD context name: *contIntegration*

### ~~CitationCount~~
An integer value indicating the number of times that the software has been cited.

Usage of this concept has ben discontinued as this value is not time invariant, and could
become meaningless the moment it is serialized to a CodeMeta instance file.

### CodeRepositoryLink
A URL for the source code repository that contains the software source files.

JSON-LD context name: *codeRepository*

### ControlledTerm
Keywords associated with the software (i.e. fixed vocabulary by which to describe a category or community of software)

JSON-LD context name: *controlledTerms*

### DateCreated
The date that a published version of the software was created by the software author.

JSON-LD context name: *dateCreated*

### DateModified
The date that a published version of the software was updated by the software author.

JSON-LD context name: *dateModified*

### DatePublished
The date the software was first made available  publicly by the publisher.

JSON-LD context name: *datePublished*

### Dependency
The computer hardware and software required to run the software.

JSON-LD context name: *dependency*

### Description
A character string conveying the purpose and scope of the software.

JSON-LD context name: *description*

### DevelopmentStatus
A designation of the current state of the software in the development lifecycle, e.g. (“active”, “inactive”) or (“beta”, “candidate release”, “release”), etc.

JSON-LD context name: *developmentStatus*

### ~~DocsCoverage~~
An indication of the completeness of documentation that describes the installation, operation and intended usage of the software. This value is expressed as a percentage."

Usage of this term has been discontinued because it does not appear in any of the schemas in the
CodeMeta crosswalk.

### ~~DownloadCount~~
An integer value indicating the number of times that the software has been downloaded.

Usage of this concept has ben discontinued as this value is not time invariant, and could
become meaningless the moment it is serialized to a CodeMeta instance file.

### DownloadLink
The URL to obtain the distribution of the software from.

JSON-LD context name: *downloadLink*

### EmbargoDate
A calendar date specifying the end of a restricted access period, i.e. the date that the software may be made publicly available.

JSON-LD context name: *embargoDate*

### Function
The role or objective associated with the software.

Usage of this term has been discontinued as there is no clear mapping to any schema in the
CodeMeta crosswalk.

### Funding
An institution, organization or other entity that has provided monetary resources needed to develop, test, distribute or support the software.

JSON-LD context name: *funding*

### ~~GeneratedBy~~
This field indicates the entity that created this metadata record (could be person or tool?)

Usage of this term has been discontinued as there is no clear mapping to any schema in the
CodeMeta crosswalk.

### ~~IdentifierNamespace~~
The authority from which the software identifier was created,  e.g. doi.org, or cran.r-project.org

Usage of this term has been discontinued because it does not appear in any of the schemas in the
CodeMeta crosswalk.

### ~~Inputs~~
Data, configuration or other types of objects used by the software.

Usage of this term has been discontinued as it is out of scope for this project.

### ~~IntendedAudience~~
The category of users that the software was designed for.

Usage of this term has been discontinued because it does not appear in any of the schemas in the
CodeMeta crosswalk.

### ~~interactionMethod~~
The interface by which a user or other agent uses the software, for example "command line interpreter",
"graphical user interface", "Application Programming Interface", etc.

Usage of this term has been discontinued as there is no clear mapping to any schema in the
CodeMeta crosswalk.

### IsAutomated
A logical value (true/false) indicating whether an update to the *CodeRepository* will trigger a new executable version of the software to be generated.

JSON-LD context name: *isAutomatedBuild*

### IsMaintainer
A logical value (true/false) indicating whether an agent (SoftwareAuthor, SoftwareContributor, etc.) is the active maintainer of the software.

JSON-LD context name: *isMaintainer*

### IsRightsHolder
A logical value (true/false) indicating whether an agent is the current agent that is the rights holder of the software, for example, does the user own the account related to the software in a source code repository, etc.

JSON-LD context name: *isRightsHolder*

### IssueLink
A URL for the issue tracking system used to report problems and request features, etc., for the software.

JSON-LD context name: *issueTracker*

### ~~L10n~~
A list of the specific counties or regions that the software has been adapted to, e.g. “en-GB,en-US,zh-CN,,zh-TW” (if using the ISO 639-1 standard codes).

Usage of this term has been discontinued because it does not appear in any of the schemas in the
CodeMeta crosswalk.

### License
The name of the license agreement governing the use and redistribution of the software. e.g. “Apache-2.0”, “GPL-3.0”, “LGPL-3.0”

JSON-LD context name: *licenseId*

### MustBeCited
A logical value (true/false) indicating that an agent must be included in a citation of the software.

JSON-LD context name: *mustbeCited*

### ~~ObjectType~~
The category of the resource (controlled list, such as software, paper, data, image) that the software can be included in.

JSON-LD context name: *@type*

### OperatingSystem
The computer system types that the software successfully operates on, i.e. “Mac OS X 10.5”, “Windows 7”"

JSON-LD context name: *operatingSystem*

### ~~Outputs~~
Data, graphics and other objects generated by usage of the software.

Usage of this term has been discontinued as it is out of scope for this project.

### ~~Package~~
Usage of this term has been discontinued as there is no clear mapping to any schema in the
CodeMeta crosswalk

### ProgrammingLanguage
The computer language that the software is implemented with.

JSON-LD context name: *programmingLanguage*

### Publisher
The institution, organization or other entity that has made a distributable version of the software publicly available.

JSON-LD context name: *publisher*

### ReadmeLink
A URL for the file that provides general information about the software.

JSON-LD context name: *readme*

### ~~RecordDateCreated~~
The date that this metadata record describing the software was created

Usage of this term has been discontinued because it does not appear in any of the schemas in the
CodeMeta crosswalk.

### ~~RecordDateModified~~
The date that this metadata record describing the software was last modified

Usage of this term has been discontinued because it does not appear in any of the schemas in the
CodeMeta crosswalk.

### ~~RecordDatePublished~~
The date that the metadata record describing the software was published

Usage of this term has been discontinued because it does not appear in any of the schemas in the
CodeMeta crosswalk.

### RelatedLink
A URL that provides additional information or resources related to the software.

JSON-LD context name: *relatedLink*

### RelatedPublications
Publications that cite the software or describe some related aspect of it.

JSON-LD context name: *relatedPublications*

### Relationship
Relationship of the software to other related resources. For example, this relationship
might be how one software package relates to a larger suite, or how a software package
version supercedes a previous version. The CodeMeta Developer Guide provides further information on the
types of relationships that are recommended, but not required, by the CodeMeta project.

JSON-LD context name: *relationship*

### Role
The function assumed or part played by a person or organization in relation to creation of the software.

Usage of this term has been discontinued as it is out of scope for this project.

### ~~SoftwareAuthor~~
The agent (person or organization) that created the software.

This term has been superceded by *Agent*.

### ~~SoftwareCitation~~
A text string that can be used to authoritatively cite the software from a published work, such as a research paper or  conference proceedings, etc.

Usage of this term has been discontinued because many different citation formats would need to be included. Instead, the fields that
are the components of a citation can be used to compose a citation from a CodeMeta document. See the [CodeMeta Tutorial](https://raw.githubusercontent.com/codemeta/codemeta/master/tutorial.md)
for examples of creating citations from a CodeMeta document.

### ~~SoftwareContributor~~
The institutions, organizations, other groups or individuals, other that the author, that assisted in authoring, designing, testing etc., of the software."

This term has been superceded by *Agent*

### SoftwareIdentifier
A universally unique character string associated with the software.

JSON-LD context name: *identifier*

### SoftwarePaperCitation
A text string that can be used to authoritatively cite a research paper, conference proceedings or other scholarly work that describes the design, development, usage, significance or other aspect of the software.

JSON-LD context name: *softwarePaperCitation*

### SoftwareTitle
The distinguishing name associated with the software.

JSON-LD context name: *title*

### Suggestions
External software components that could enhance operation of or enable advanced functionality of the software package but are not strictly required.

JSON-LD context name: *suggestions*

### Tags
Terms used to describe the software that facilitate discovery of the software.

JSON-LD context name: *tags*

### ~~TestCoverage~~
An indication of the completeness of testing methods (scripts, data, etc.) that verify the correct operation of the software. This value is expressed as a percentage.

Usage of this term has been discontinued because it does not appear in any of the schemas in the
CodeMeta crosswalk.

### UploadedBy
The user identity that uploaded the software to an online repository.

JSON-LD context name: *uploadedBy*

### Version
A unique string indicating a specific state of the software, i.e. an initial public release, an update or bug fix release, etc. No version format or schema is enforced for this value."

JSON-LD context name: *version*

### ZippedCodeLink
A URL for the software distribution in compressed form.

JSON-LD context name: *zippedCode*
