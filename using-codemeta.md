
# CodeMeta Software Metadata

## CodeMeta Overview

The CodeMeta project strives to promote the reuse of software authored for scientific research by developing a mechanism to assist the transfer of software and software descriptions (metadata) between the entities that author, archive, distribute, aggregate citations and use the software. Our approach is not to create a new metadata standard or schema, but instead to define a crosswalk between existing software metadata schemas, and to provide a uniform method to package and transfer this metadata between entities.

(A complete description of the CodeMeta project can be found here https://github.com/codemeta/codemeta-paper.)

The mechanism to package and transfer software descriptions that the CodeMeta project has adopted uses JSON-LD,
which is a W3C standard that enables JSON based documents to be universally understandable and processable
by adhering to principles outlined for [linked data](https://en.wikipedia.org/wiki/Linked_data):

- Use URIs to name (identify) things.
- Use HTTP URIs so that these things can be looked up (interpreted, "dereferenced").
- Provide useful information about what a name identifies when it's looked up, using open standards such as RDF, SPARQL, etc.
- Refer to other things using their HTTP URI-based names when publishing data on the Web.

JSON-LD is a W3C standard, specified at https://www.w3.org/TR/json-ld/

## CodeMeta Metadata Usage

JSON-LD uses a *context file* to associate JSON names with an IRI (Internationalized Resource Identifier).  The JSON names then serve as abbreviated, local names for the IRIs that are universally unique identifiers for concepts from widely used schemas such as schema.org and Dublin Core.

The context file *codemeta.jsonld* contains the complete set of JSON properties adopted by the CodeMeta project.

A CodeMeta software description, or *instance file*, references the context file by using the JSON names, which are more compact and easier to process than IRIs.

Because the instance file referes the context file, the mapping between the local JSON names and the IRIs is always
known, thereby giving the local names universal context.

An example usage of CodeMeta instance file is for a software package author to generate an instance file when a software package is published to a repository, so that the software description can be used to aid in the repository ingest processing.

The producer of an instance file, i.e. the creators of the software, must use the JSON names from the CodeMeta context file. The consumer of the instance file can use the JSON names from the instance file for any necessary processing tasks.

As an alternative to using the producer supplied JSON names, the consumer can use the JSON-LD API to translate the JSON names to their own local JSON names that may be in use by their local processing scripts. This is done by first using the JSON-LD *expand* function that replaces each JSON name with it's corresponding IRI from the CodeMeta context file. For example, the producer's instance file may contain the following line:

      "codeRepository":"https://github.com/DataONEorg/rdataone"

Using the JSON-LD API *expand* function, this is converted to:

     "http://schema.org/repository":"https://github.com/DataONEorg/rdataone

Next, the consumer can use their own context file that maps from each IRI to their own local JSON names. For example, the consumer may have a context file that maps the local JSON name 'softwareRepo' to "http://schema.org/repository", so using the JSON API *compact* function would result in a new instance file with the entry:

     "softwareRepo":"https://github.com/DataONEorg/rdataone"

When the instance file has been compacted, it can then be used by the consumer for any necessary processing, using the local JSON names.

Note that this expansion and compaction process assumes that both the producer and consumer JSON-LD context files share overlapping sets of IRIs.

## Creating A CodeMeta Instance File

Tools will be created by data repositories and aggregators such as the CodeMeta participants, to author CodeMeta instance files for software packages. For example, one of the goals of the CodeMeta project is to author a tool that creates a CodeMeta instance file from a published R package. R package authors go through a lengthy process to prepare metadata that is needed to publish their software in repositories such as CRAN. This metadata is available from CRAN and could be used to prepare a CodeMeta instance file such as the one shown in Appendix B.

The following points may assist in the building of such tools, or alternatively for the manual authoring of instance files.

The example document in Appedix B can be used as a starting point in authoring an instance file.

CodeMeta instance files contain JSON name, value pairs where the values can be simple values, arrays or JSON objects. A simple value is a number, string, or one the literal values *false*, *null* *true*, for example:

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
   "email":"slaughter@nceas.ucsb.edu",
   "name":"Peter Slaughter"
}
```

The "uploadedBy" JSON object illustrates the use of the JSON-LD keyword "@id", which is used to associate.

Appendix A provides a list of CodeMeta concepts and the corresponding JSON names.

[This section needs more content]

## JSON-LD Relationship to RDF

The intent of JSON-LD is to provide a mechanism to represent linked data using JSON syntax, yet JSON-LD was developed as a W3C Standard by the  RDF Working Group. Even though JSON-LD can be effectively used without converting a JSON-LD document to RDF, it is useful to consider the relationship of JSON-LD to RDF in order to fully understanding JSON-LD.

(Because this technology is RDF-centric, the process of converting a JSON-LD file to RDF is termed "deserializing JSON-LD to RDF", as explained in the JSON-LD 1.0 [Processing Algorithms and API](JSON-LD 1.0 Processing Algorithms and API).)

For example, in the instance file, the JSON-LD "@id" keyword is used to associate an IRI with a JSON object. When the JSON-LD instance file is deserialized to RDF, this becomes the graph node identifier, or the subject of the resulting RDF triple. If an @id is not specified for a JSON object, then a blank node identifier is assigned to the resulting graph node for the output RDF graph.

## Appendix A - CodeMeta Properties

The following set of JSON properties have been selected and vetted by the CodeMeta project for use in creating software descriptions that can be used to transfer metadata between participating CodeMeta partners and others, for the purposes of archiving, sharing, indexing, citing and discovering software.

Note that the following namespace abbreviations are used in the CodeMeta context file, and referenced in this section:

- "schema" : "http://schema.org/",
- "dcterms" : "http://purl.org/dc/terms/",
- "xsd" : "http://www.w3.org/2001/XMLSchema#",
- "codemeta" : "https://codemeta.github.io/terms/",

### affiliation
Context IRI: schema:affiliation  
Type: xsd:string
Subproperties: None

An *affliation* is the institution, organization or other group that the software creator is associated with.

### agent
Context IRI: schema:agent  
Type: schema:Organization, schema:Person  
Subproperties: @id, @type, email, name, affiliation, isCitable, isMaintainer, isRightsHolder, role

An *agent* is an organization or person that is in some way related to the creation of the software. An *agent* can be assigned a @type of *schema:Organization* or *schema:Person*.

Note that the names *person* and *organization* are defined in the CodeMeta context file and can be used as abbreviated forms for the schema.org types.

An array of values can be assigned to the property *agent*, but each should have an "@id" and "@type" assigned.

### @id

The JSON-LD keyword "@id" is used to associate a JSON object with an IRI.

### buildInstructions
Context IRI: codemeta:buildInstructions
Type: xsd:anyURI
Subproperties: @id, @type, email, name, affiliation, isCitable, isMaintainer, isRightsHolder, role

### contIntegration  
Context IRI: codemeta:contIntegration  
Type: xsd:anyURI  
Subproperties: None

A URL for the continuous integration system used to build the software automatically after updates to the source code repository.

### codeRepository
Context IRI: schema:codeRepository  
Type: schema:URL  
Subproperties: None

### controlledTerm
Context IRI: codemeta:controlledTerm  
Type: xsd:string  
Subproperties: None

### dateCreated
Context IRI: schema:dateCreated
Type: xsd:dateTime
Subproperties: None  

### dateModified
Context IRI: schema:dateCreated
Type: xsd:dateTime
Subproperties: None  

### datePublished
Context IRI: schema:dateCreated  
Type: xsd:dateTime  
Subproperties: None  

### dependency
Context IRI:
Type:
Subproperties:

### description
Context IRI:
Type:
Subproperties:

### docsCoverage
Context IRI:
Type:
Subproperties:

### downloadCount
Context IRI:
Type:
Subproperties:

### downloadLink
Context IRI:
Type:
Subproperties:

### email
Context IRI:
Type:
Subproperties:

### embargoDate
Context IRI:
Type:
Subproperties:

### function
Context IRI:
Type:
Subproperties:

### funding
Context IRI:
Type:
Subproperties:

### inputs
Context IRI:
Type:
Subproperties:

### interactionMethod
Context IRI:
Type:
Subproperties:

### isAutomatedBuild
Context IRI:
Type:
Subproperties:

### isCitable
Context IRI:
Type:
Subproperties:

### isMaintainer
Context IRI:
Type:
Subproperties:

### isRightsHolder
Context IRI:
Type:
Subproperties:

### issueTracker
Context IRI:
Type:
Subproperties:

### license
Context IRI:
Type:
Subproperties:

### name
Context IRI:
Type:
Subproperties:

### objectType
Context IRI:
Type:
Subproperties:

### outputs
Context IRI:
Type:
Subproperties:

### programmingLanguage
Context IRI:
Type:
Subproperties:

### publisher
Context IRI:
Type:
Subproperties:

### readme
Context IRI:
Type:
Subproperties:

### relatedLink
Context IRI:
Type:
Subproperties:

### relatedPublications
Context IRI:
Type:
Subproperties:

### relationship
Context IRI:
Type:
Subproperties:

### author
Context IRI:
Type:
Subproperties:

### softwareCitation
Context IRI:
Type:
Subproperties:

### contributor
Context IRI:
Type:
Subproperties:

### identifier
Context IRI:
Type:
Subproperties:

### softwarePaperCitation
Context IRI:
Type:
Subproperties:

### title
Context IRI:
Type:
Subproperties:

### suggests
Context IRI:
Type:
Subproperties:

### tags
Context IRI:
Type:
Subproperties:

### testCoverage
Context IRI:
Type:
Subproperties:

### uploadedBy
Context IRI:
Type:
Subproperties:

### version
Context IRI:
Type:
Subproperties:

### zippedCode
Context IRI:
Type:
Subproperties:


## Glossary

### CodeMeta
### context file
### Instance file
### IRI
### JSON object

## Appendix B Example Description File

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
      }
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
