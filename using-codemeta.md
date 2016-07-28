
# CodeMeta Software Metadata

## CodeMeta Overview

The CodeMeta project strives to promote the citation and reuse of software authored for scientific research by developing a mechanism to assist the transfer of software and software metadata between the entities that author, archive, index and distribute and use the software. Our approach is not to create a new metadata standard or schema, but instead to define a crosswalk between existing software metadata schemas, and to provide a uniform method to package and transfer this metadata between entities.

(A complete description of the CodeMeta project can be found here https://github.com/codemeta/codemeta-paper.)

The mechanism to package and transfer software descriptions that the CodeMeta project has adopted uses [JSON-LD](http://json-ld.org/),
which is a W3C standard that enables JSON based documents to be universally understandable and processable
by adhering to principles outlined for linked data](https://en.wikipedia.org/wiki/Linked_data):

- Use URIs to name (identify) resources so that they can be located and retrieved.
- Provide useful information about what a name identifies when it's looked up, using open standards.
- Refer to other things using their HTTP URI-based names when publishing them on the Web.

The JSON-LD [Best Practices guide](http://json-ld.org/spec/latest/json-ld-api-best-practices/) describes linked data as:

> Linked Data is a way to create a network of standards-based machine interpretable data
> across different documents and Web sites. It allows an application to start at one piece of Linked
> Data, and follow embedded links to other pieces of Linked Data that are hosted on different
> sites across the Web."

JSON-LD is a W3C standard, specified at https://www.w3.org/TR/json-ld/

## CodeMeta Metadata Usage

JSON-LD uses a *context file* to associate JSON names with IRIs (Internationalized Resource Identifier).  The JSON names then serve as abbreviated, local names for the IRIs that are universally unique identifiers for concepts from widely used schemas such as [schema.org](http://schema.org) and [Dublin Core Metadata Element Set](http://dublincore.org/documents/dces/).

The context file [*codemeta.jsonld*](https://raw.githubusercontent.com/codemeta/codemeta/master/codemeta.jsonld) contains the complete set of JSON properties adopted by the CodeMeta project.

A CodeMeta software description, or *instance file*, uses the JSON names contained in the context file. The JSON names are more compact and easier to process than IRIs. The instance files can be used to transfer metadata between software authors, repositories, and others, for the purposes of archiving, sharing, indexing, citing and discovering software.

Because the instance file refers to the context file, the mapping between the local JSON names and the
IRIs is always known, thereby giving the local names universal context.

An example usage of the CodeMeta instance file is for the author of research software package to generate an instance file when the software package is published to a repository. The instance file can be used to aid in any repository ingest processing. The instance file can be made available in the repository with the software package as it may contain additional metadata that was not used by the repository. In addition this file may be used in other transactions involving the software package after the package has been downloaded from the repository.

The producer of an instance file, i.e. the creators of the software, must use the JSON names from the CodeMeta context file. The consumer of the instance file can use these same JSON names from the instance file for any necessary processing tasks.

As an alternative to using the producer supplied JSON names, the consumer can use the [JSON-LD API](https://www.w3.org/TR/json-ld-api/) to translate the JSON names to their own local JSON names that may be in use by their local processing scripts. This is done by first using the JSON-LD *expand* function that replaces each JSON name in the instance file with it's corresponding IRI from the CodeMeta context file. For example, the producer's instance file may contain the following line:

      "codeRepository":"https://github.com/DataONEorg/rdataone"

Using the JSON-LD API *expand* function, this is converted to:

     "http://schema.org/repository":"https://github.com/DataONEorg/rdataone

Next, the consumer can use their own context file that maps from each IRI to their own local JSON names. For example, the consumer may have a context file that maps the local JSON name 'softwareRepo' to "http://schema.org/repository", so using the JSON API *compact* function would result in a new instance file with the entry:

     "softwareRepo":"https://github.com/DataONEorg/rdataone"

When the instance file has been compacted, it can then be used by the consumer for any necessary processing, using the local JSON names.

Note that this expansion and compaction process assumes that both the producer and consumer JSON-LD context files share overlapping sets of IRIs.

## Creating A CodeMeta Instance File

To facilitate automated ingest of research software into repositories such as [figshare](https://figshare.com/), [Zenodo](https://zenodo.org/), the [Knowledge Network for Biocomplexity](https://knb.ecoinformatics.org/) and others, these repositories will update
their submission processes to use CodeMeta instance files which will provide the metadata necessary for the submission and indexing of the software.

Tools will be created that assist in the generation of instance files. For example, a tool written in the R language would generate a CodeMeta instance file from an R package that was authored to support a research project, automatically collecting available metadata and possibly prompting the user for any additional required metadata. The instance file would then be used to assist in publishing the software to a repository. An example instance file is shown in Appendix C.

When creating an instance file, note that they contain JSON name, value pairs where the values can be simple values, arrays or JSON objects. A simple value is a number, string, or one the literal values *false*, *null* *true*, for example:

```
    "title" : "R Interface to the DataONE REST API"
```

A JSON array is surrounded by the characters `[` and `]`, and can contain multiple values:

```
"tags": [ "data sharing", "data repository", "DataONE" ]
```

A JSON object is surrounded by curly braces and can contain other JSON values or objects, for example:
```
"uploadedBy":{
   "@id":"http://orcid.org/0000-0003-0077-4738",
   "@type":"person",
   "email":"slaughter@nceas.ucsb.edu",
   "name":"Peter Slaughter"
}
```

The "uploadedBy" JSON object illustrates the use of the JSON-LD keyword "@id", which is used to associate an IRI with the JSON object.

The JSON "@type" keyword associates a JSON value or object with a well known type, for example, the
statement `"@type":"person"` associates the `uploadedBy` object with `http://schema.org/`.

For a list of the JSON names that can be used in a CodeMeta instance file, see Appendix B.

## Minimal Instance File

 [ TBD ]

## Testing An Instance file

 [ TBD ]

## Appendix A JSON-LD Relationship to RDF

The intent of JSON-LD is to provide a mechanism to represent linked data using standard JSON syntax, yet JSON-LD was developed as a W3C Standard by the RDF Working Group. Even though JSON-LD can be effectively used without converting a JSON-LD document to RDF, it is useful to consider the relationship of JSON-LD to RDF in order to fully understanding JSON-LD.

For example, in the instance file, the JSON-LD "@id" keyword is used to associate an IRI with a JSON object. When the JSON-LD instance file is serialized to RDF, this becomes the graph node identifier, or the subject of the resulting RDF triple. If an @id is not specified for a JSON object, then a blank node identifier is assigned to the resulting graph node for the output RDF graph. The JSON object `role` from the example
instance file:

```
      "roleCode":[
         "originator",
         ...
      ]
```

is serialized to RDF as:

```
_:b1 <https://codemeta.github.io/terms/roleCode> "originator" .
```

When the JSON-LD "@type" keyword is applied to a simple JSON type, the serialized RDF will have that type appended to the object, for example, the following entry from the example instance file:

```
"dateCreated":"2016-05-27"
```

is serialized to the following RDF ([N-Triples format](https://www.w3.org/TR/n-triples/)):

```
_:b0 <http://schema.org/dateCreated> "2016-05-27"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
```

In this case, the "@type" was specified in the context file.

When the JSON-LD "@type" is applied to a JSON object, the type information is serialized to RDF with
an RDF type statement, for example, this JSON object from the sample instance file:

```
"agent":[
  {
     "@id":"http://orcid.org/0000-0002-3957-2474",
     "@type":"organization",
    ...

  }
]
```

is serialized to RDF as:

```
<http://orcid.org/0000-0002-3957-2474> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Organization> .

```

This example shows the "@type" keyword being used in the instance file. Because `agent` can be one
of multiple possible types ("person", "organization") the type must be defined for each instance.

## Appendix B - CodeMeta Properties

[ Need to include examples for any term where appropriate ]

The following set of JSON-LD properties have been selected and vetted by the CodeMeta project for use in creating Codemeta instance files.

Note that the following namespace abbreviations are used in the CodeMeta context file, and referenced in this section:

- "schema" : "http://schema.org/",
- "dcterms" : "http://purl.org/dc/terms/",
- "xsd" : "http://www.w3.org/2001/XMLSchema#",
- "codemeta" : "https://codemeta.github.io/terms/",

### affiliation
Context IRI: schema:affiliation  
Type: xsd:string  
Subproperties: None

An *affliation* is the institution, organization or other group that the software agent is associated with.

### agent
Context IRI: schema:agent  
Type: schema:Organization, schema:Person  
Subproperties: @id, @type, email, name, affiliation, isCitable, isMaintainer, isRightsHolder, role

An *agent* is an organization or person that is in some way related to the creation of the software. An *agent* can be assigned a @type of *schema:Organization* or *schema:Person*.

Note that the names *person* and *organization* are defined in the CodeMeta context file and can be used as abbreviated forms for the schema.org types.

An array of values can be assigned to the property *agent*, but each should have an "@id" and "@type" assigned.

```
 "agent":[
      {
         "@id":"http://orcid.org/0000-0003-0077-4738",
         "@type":"Person",
         "email":"jones@nceas.ucsb.edu",
         "name":"Matt Jones",
         "affiliation":"NCEAS",
         "isCitable":true,
         "isMaintainer":false,
         "isRightsHolder":true,
         "role":[
            {
               "namespace":"http://www.ngdc.noaa.gov/metadata/published/xsd/schema/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
               "roleCode":[
                  "originator",
                  "resourceProvider"
               ]
            }
         ]
      },
      {
         "@id":"http://orcid.org/0000-0002-3957-2474",
         "@type":"Organization",
         "email":"info@ucop.edu",
         "name":"University of California, Santa Barbara",
         "role":[
            {
               "namespace":"http://www.ngdc.noaa.gov/metadata/published/xsd/schema/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
               "roleCode":"copyrightHolder"
            }
         ]
      }
```

### @id

The JSON-LD keyword "@id" is used to associate a JSON object with an IRI.

### buildInstructions
Context IRI: codemeta:buildInstructions  
Type: xsd:anyURI  
Subproperties: @id, @type, email, name, affiliation, isCitable, isMaintainer, isRightsHolder, role

A URL for the instructions to create an executable version of the software from source code.

### contIntegration  
Context IRI: codemeta:contIntegration  
Type: xsd:anyURI  
Subproperties: None

A URL for the continuous integration system used to build the software automatically after updates to the source code repository.

### codeRepository
Context IRI: schema:codeRepository  
Type: schema:URL  
Subproperties: None

A URL for the repository containing the software source files.

### controlledTerm
Context IRI: codemeta:controlledTerm  
Type: xsd:string  
Subproperties: None

Keywords associated with the software (i.e. Fixed vocabulary by which to describe category or community of software)

### dateCreated
Context IRI: schema:dateCreated  
Type: xsd:dateTime  
Subproperties: None  

The date that a published version of the software was created by the software author.

### dateModified
Context IRI: schema:dateCreated  
Type: xsd:dateTime  
Subproperties: None  

The date that a published version of the software was updated by the software author.

### datePublished
Context IRI: schema:dateCreated  
Type: xsd:dateTime  
Subproperties: None  

The date the software was first made publicly available.

### dependency
Context IRI: schema:requirements  
Type: Not assigned  
Subproperties: None

The computer hardware and software required to run the software.

### description
Context IRI: chema:description  
Type: xsd:string  
Subproperties: None

A text representation conveying the purpose and scope of the software.

### docsCoverage
Context IRI: codemeta:docsCoverage  
Type: xsd:string  
Subproperties: None

An indication of the completeness of documentation that describes the installation, operation and intended usage of the software. This value is expressed as a percentage.

### downloadLink
Context IRI: schema:downloadUrl  
Type: xsd:anyURI  
Subproperties:

The URL to obtain the distribution of the software from.

### email
Context IRI: schema:email  
Type: xsd:string  
Subproperties:

The email address associated with a software agent.

### embargoDate
Context IRI: codemeta:embargoDate  
Type: xsd:dataTime  
Subproperties: None

A calendar date specifying the end of a restricted access period, i.e. the date that the software may be made publicly available.

### function
Context IRI: codemeta:function  
Type: xsd:string  
Subproperties: None

The role or objective associated with the software.

### funding
Context IRI: codemeta:funding  
Type: xsd:string  
Subproperties: None

An institution, organization or other entity that has provided the resources needed to develop, test, distribute and support the software.

### inputs
Context IRI: codemeta:inputs  
Type: xsd:string  
Subproperties: None

Data, configurations or other types of objects used by the software.

### interactionMethod
Context IRI: codemeta:interactionMethod  
Type: xsd:string  
Subproperties: None

How a user or software system uses the software, for example:  Command-line, GUI, Excel..

### isAutomatedBuild
Context IRI: codemeta:isAutomatedBuild  
Type: xsd:boolean  
Subproperties: None

A logical value (true/false) indicating whether an update to the CodeRepository will trigger a new executable version of the software to be generated.

### isCitable
Context IRI: codemeta:isCitable  
Type: xsd:boolean  
Subproperties: None

A logical value (true/false) indicating whether an agent (author, contributor, etc) can be included in a citation of the software.

### isMaintainer
Context IRI: codemeta:isMaintainer  
Type: xsd:boolean  
Subproperties: None

A logical value (true/false) indicating whether an agent (SoftwareAuthor, SoftwareContributor, etc.) is the active maintainer of the software

### isRightsHolder
Context IRI: codemeta:isRightsHolder  
Type: xsd:boolean  
Subproperties: None

A logical value (true/false) indicating whether an agent is the current rights holder of the software

### issueTracker
Context IRI: codemeta:issueTracker  
Type: xsd:anyURI  
Subproperties: None

A URL for the issue tracking system used to report problems and request features, etc., for the software.

### license
Context IRI: schema:license  
Type: xsd:string  
Subproperties: None

The name of the license agreement governing the use and redistribution of the software. e.g. “Apache 2”, “GPL”, “LGPL”

### name
Context IRI: schema:name  
Type: xsd:string  
Subproperties: None

The name of the institution, organization, individuals or other entities that had a role in the creation of the software.

### objectType
Context IRI: dc:type  
Type: xsd:string  
Subproperties: None

The category of the resource (controlled list, such as software, paper, data, image) that is associated with the software.

### outputs
Context IRI: codemeta:outputs  
Type: xsd:string  
Subproperties: None

Data, graphics and other objects generated by usage of the software.

### programmingLanguage
Context IRI: schema:programmingLanguage  
Type: Not assigned  
Subproperties: name, version, URL

The computer language that the software is implemented with.

### publisher
Context IRI: schema:publisher  
Type: xsd:string  
Subproperties: None

The institution, organization or other entity that makes a distributable version of the software publicly available.

### readme
Context IRI: codemeta:readme  
Type: xsd:anyURI  
Subproperties: None

A URL for the file that provides general information about the software.

### relatedLink
Context IRI: codemeta:relatedLink  
Type: xsd:anyURI  
Subproperties: None

A URL that provides additional information or resources related to the software.

### relatedPublications
Context IRI: codemeta:relatedPublications  
Type: xsd:string  
Subproperties: None

Publications that cite the software or describe some aspect of it.

### relationship
Context IRI: codemeta:relationship  
Type: xsd:string  
Subproperties: None

Relationship of the software to other related resources

### role
Context IRI: codemeta:relationship  
Type: @id  
Subproperties: roleCode

A function or part performed by an agent.

### roleCode
Context IRI: codemeta:roldCode  
Type: xsd:string  
Subproperties: None

The identifier that defines a specific role.

Example:
```
"roleCode":[
   "originator",
   "resourceProvider"
]
```

### softwareCitation
Context IRI: codemeta:softwarePaperCitation  
Type: xsd:string  
Subproperties: None

A text string that can be used to authoritatively cite the software from a published work, such as a research paper or conference proceedings, etc.

### identifier
Context IRI: dcterms:identifier  
Type: xsd:anyURI  
Subproperties: None

A universally unique character string associated with the software.

### softwarePaperCitation
Context IRI: codemeta:softwarePaperCitation  
Type: xsd:string  
Subproperties: None

A text string that can be used to authoritatively cite a research paper, conference proceedings or other scholarly work that describes the design, development, usage, significance or other aspect of the software.

### title
Context IRI: dcterms:title  
Type: xsd:string  
Subproperties: None

The distinguishing name associated with the software.

### suggests
Context IRI: schema:suggests  
Type: xsd:string  
Subproperties: None

External software components that could enhance operation of or enable advanced functionality of the software package but is not strictly required.

### tags
Context IRI: schema:keywords  
Type: xsd:string  
Subproperties: None

Terms used to describe the software that facilitate discovery of the software.

### testCoverage
Context IRI: codemeta:testCoverage  
Type: xsd:integer  
Subproperties: None

An indication of the completeness of testing methods (scripts, data, etc.) that verify the correct operation of the software. This value is expressed as a percentage.

### uploadedBy
Context IRI: codemeta:uploadedBy  
Type: Not specified  
Subproperties: @id, email, name

The user identity that uploaded the software to an online repository.

### version
Context IRI: schema:version  
Type: xsd:string  
Subproperties: None

A unique string indicating a specific state of the software, i.e. an initial public release, an update or bug fix release, etc. No version format or schema is enforced for this value.

### zippedCode
Context IRI: codemeta:zippedCode  
Type: xsd:anyURI  
Subproperties: None

ZippedCodeLink  A URL for the software distribution in compressed form.


## Appendix C Example Description File

The following JSON-LD document was created to describe the [*dataone* R package]( https://cran.r-project.org/web/packages/dataone/index.html ).

```
{
   "@context":"https://raw.githubusercontent.com/codemeta/codemeta/master/codemeta.jsonld",
   "@type":"Code",
   "agent":[
      {
         "@id":"http://orcid.org/0000-0003-0077-4738",
         "@type":"person",
         "email":"jones@nceas.ucsb.edu",
         "name":"Matt Jones",
         "affiliation":"NCEAS",
         "isCitable":true,
         "isMaintainer":true,
         "isRightsHolder":true,
         "role":[
            {
               "namespace":"http://www.ngdc.noaa.gov/metadata/published/xsd/schema/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
               "roleCode":[
                  "originator",
                  "resourceProvider"
               ]
            }
         ]
      },
      {
         "@id":"http://orcid.org/0000-0002-2192-403X",
         "@type":"person",
         "email":"slaughter@nceas.ucsb.edu",
         "name":"Peter Slaughter",
         "affiliation":"NCEAS",
         "isCitable":true,
         "isMaintainer":false,
         "isRightsHolder":false,
         "role":{
            "namespace":"http://www.ngdc.noaa.gov/metadata/published/xsd/schema/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
            "roleCode":"contributor"
         }
      },
      {
         "@id":"http://orcid.org/0000-0002-3957-2474",
         "@type":"organization",
         "email":"info@ucop.edu",
         "name":"University of California, Santa Barbara",
         "role":{
            "namespace":"http://www.ngdc.noaa.gov/metadata/published/xsd/schema/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
            "roleCode":"copyrightHolder"
         }
      }
   ],
   "dependency":
      {
         "@type":"URL",
         "@value":"https://github.com/ropensci/datapack"
  },
   "identifier":"http://dx.doi.org/10.5063/F1M61H5X",
   "codeRepository":"https://github.com/DataONEorg/rdataone",
   "controlledTem": "software",
   "datePublished":"2016-05-27",
   "dateModified":"2016-05-27",
   "dateCreated":"2016-05-27",
   "description":"Provides read and write access to data and metadata from
    the DataONE network of data repositories.  Each DataONE repository
    implements a consistent repository application programming interface.
    Users call methods in R to access these remote repository functions,
    such as methods to query the metadata catalog, get access to
    metadata for particular data packages, and read the data objects from
    the data repository. Users can also insert and update data objects on
    repositories that support these methods.",
   "downloadLink":"https://cran.r-project.org/src/contrib/dataone_2.0.0.tar.gz",
   "function":"Provides an R Interface to the DataONE REST API",
   "funding":"National Science Foundation grant #012345678",
   "isAutomatedBuild":false,
   "issueTracker":"https://github.com/DataONEorg/rdataone/issues",
   "license":"http://opensource.org/licenses/Apache2",
   "publisher":"https://cran.r-project.org"
   "tags":[
      "data sharing",
      "data repository",
      "DataONE"
   ],
   "title":"R Interface to the DataONE REST API",
   "version":"2.0.0",
   "uploadedBy":{
      "@id":"http://orcid.org/0000-0003-0077-4738",
      "@type":"person",
      "email":"mbjones@nceas.ucsb.edu",
      "name":"Matt Jones"
   },
   "objectType":"software",
   "programmingLanguage":{
      "name":"R",
      "version":"> 3.1.1",
      "URL":"https://www.r-project.org"
   },
   "readme":"https://github.com/DataONEorg/rdataone/README.md",
   "softwareCitation":"Jones M, Slaughter P, Nahf R, Jones C, Boettiger C, Walker L, Hallett L, Chamberlain S, Hart E and Read J (2016).
_redland: R Interface to the DataONE REST API_. doi: 10.5063/F1M61H5X (URL: http://doi.org/10.5063/F1M61H5X), R
package version 2.0.0, <URL: http://github.com/DataONEorg/rdataone>.",
   "zippedCode":"https://cran.r-project.org/src/contrib/dataone_2.0.0.tar.gz"
}
```
