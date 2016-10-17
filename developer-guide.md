
# CodeMeta Developer Guide

This guide is intended for software developers who require detailed information about the CodeMeta project's
usage of JavaScript Object Notation for Linked Data ([JSON-LD](http://json-ld.org/)) for defining a
methodology for creating software package descriptions. For example, this guide may be helpful for developers that are
designing software to generate or read CodeMeta JSON software descriptions.

Users that only require instructions for manually creating CodeMeta software descriptions may wish to
review the upcoming [CodeMeta Tutorial](https://github.com/codemeta/codemeta/blob/master/tutorial.md). This document
will be posted to the git repository as soon as it is available.

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
statement `"@type":"person"` associates the `uploadedBy` object with `http://schema.org/Person`.

For a list of the JSON names that can be used in a CodeMeta instance file, see Appendix B.

Every CodeMeta instance file must refer to the context file *codemeta.jsonld*, for example via a URL.
The context file may be modified and updated in the future, if new JSON properties are added or existing ones modified.
The CodeMeta github repository defines tags to allow specific versions of a file to be referenced, so that an
instance file that is making the reference will continue to be valid, even if the most current ("HEAD") version of
the file in the repository changes.

It is therefor recommended that a Github tag be used to specify a specific, non-changing version of the context file.
For example, for the "0.1-tag", the following URL could be included in an instance file:
```
    "@context":"https://raw.githubusercontent.com/codemeta/codemeta/0.1-alpha/codemeta.jsonld"
```

The tags defined for the CodeMeta github repository can be listed by viewing the web page:

    https://github.com/codemeta/codemeta/tags

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
"agents":[
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

This example shows the "@type" keyword being used in the instance file. Because each entry in `agents` can be one
of multiple possible types ("person", "organization") the type must be defined for each instance.

## Appendix B - CodeMeta Properties

The following set of JSON-LD properties have been selected and vetted by the CodeMeta project for use in creating Codemeta instance files.

The related document *codemeta-concepts.md* contains definitions for the concepts that these
JSON properties are associated with.

Note that the following namespace abbreviations are used in the CodeMeta context file, and referenced in this section:

- "schema" : "http://schema.org/",
- "dcterms" : "http://purl.org/dc/terms/",
- "xsd" : "http://www.w3.org/2001/XMLSchema#",
- "codemeta" : "https://codemeta.github.io/terms/",

### affiliation
Context IRI: schema:affiliation  
Type: xsd:string  
Subproperties: None
Associated CodeMeta Concept: *AgentAffiliation*

An *affliation* is the institution, organization or other group that the software agent is associated with.

### agents
Context IRI: schema:agent  
Type: schema:Organization, schema:Person  
Subproperties: @id, @type, email, name, affiliation, mustBeCited, isMaintainer, isRightsHolder, role  
Associated CodeMeta Concept: *Agent*

An *agent* is an organization or person that is in some way related to the creation of the software. An *agent* can be assigned a @type of *schema:Organization* or *schema:Person*.

Each instance of an *agent* must be qualified with an appropriate *role* property.

An array of values can be assigned to the property *agent*, but each should have an "@id" and "@type" assigned.

```
 "agents":[
      {
         "@id":"http://orcid.org/0000-0003-0077-4738",
         "@type":"Person",
         "email":"jones@nceas.ucsb.edu",
         "name":"Matt Jones",
         "affiliation":"NCEAS",
         "mustBeCited":true,
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
Associated CodeMeta concept: *AgentId*

The JSON-LD keyword "@id" is used to associate a JSON object with an IRI.

### buildInstructions
Context IRI: codemeta:buildInstructions  
Type: xsd:anyURI  
Subproperties: @id, @type, email, name, affiliation, mustBeCited, isMaintainer, isRightsHolder, role  
Associated CodeMeta Concept: *BuildLink*

### contIntegration  
Context IRI: codemeta:contIntegration  
Type: xsd:anyURI  
Subproperties: None  
Associated CodeMeta Concept: *CILink*

### codeRepository
Context IRI: schema:codeRepository  
Type: schema:URL  
Subproperties: None  
Associated CodeMeta Concept: *CodeRepositoryLink*

### controlledTermss
Context IRI: codemeta:controlledTerms
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *ControlledTerms*

### dateCreated
Context IRI: schema:dateCreated  
Type: xsd:dateTime  
Subproperties: None  
Associated CodeMeta Concept: *DateCreated*

### dateModified
Context IRI: schema:dateCreated  
Type: xsd:dateTime  
Subproperties: None  
Associated CodeMeta Concept: *DateModified*

### datePublished
Context IRI: schema:dateCreated  
Type: xsd:dateTime  
Subproperties: None  
Associated CodeMeta Concept: *DateModified*

### dependencies
Context IRI: schema:requirements
Type: Not assigned  
Subproperties: *identifier*, *name*, *packageSystem*, *version*, *operatingSystem*  
Associated CodeMeta Concept: *Dependency*

The *dependencies* property is used to describe software packages required by the main package in order
to run. The properties *identifier*, *name*, *packageSystem*, *version* and *operatingSystem* can be specified
for *dependencies*, for example, the following instance file fragment describes two required
software packages:

```
   ...
   "dependencies": [{
       "identifier": "http://doi.org/10.xxxx/A324566",
       "name": "export_fig",
       "version": "1.99",
       "packageSystem": "http://www.mathworks.com"
   }, {
       "identifier": "89766228838383883",
       "name": "npplus",
       "version": "0.9.4",
       "packageSystem": "https://pypi.python.org",
       "operatingSystem": ["MacOS", "Linux"]
   }],
     ...
```

The property *packageId* contains a character string that uniquely identifies a software
package for the specified *packageSystem*. The *version* specifies the software
revision that is required. The *operatingSystem* specifies the platform types that
the software is supported on, and is optional.

### description
Context IRI: schema:description  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *Description*

### downloadLink
Context IRI: schema:downloadUrl  
Type: xsd:anyURI  
Subproperties: None  
Associated CodeMeta Concept: *DownloadLink*

### email
Context IRI: schema:email  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *AgentEmail*

The email address associated with a software agent.

### embargoDate
Context IRI: codemeta:embargoDate  
Type: xsd:dataTime  
Subproperties: None  
Associated CodeMeta Concept: *EmbargoDate*

### function
Context IRI: codemeta:function  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *Function*

### funding
Context IRI: codemeta:funding  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *Funding*

The property *funding* contains a list of character strings containing funding sources for the software package. This property can
can be a single character string:

```
"funding": "National Science Foundation grant #abc",

```
or a list of multiple character strings:
```
"funding": [
    "National Science Foundation grant #abc",
    "National Science Foundation grant #def",
]
```

### identifier  
Context IRI: dcterms:identifier  
Type: xsd:string  
Subproperties: None
Parent propertes: *dependencies*, can also be at top (root) level

### isAutomatedBuild
Context IRI: codemeta:isAutomatedBuild  
Type: xsd:boolean  
Subproperties: None  
Associated CodeMeta Concept: *IsAutomated*

### mustBeCited
Context IRI: codemeta:mustBeCited  
Type: xsd:boolean  
Subproperties: None  
Associated CodeMeta Concept: *MustBeCited*

### isMaintainer
Context IRI: codemeta:isMaintainer  
Type: xsd:boolean  
Subproperties: None  
Associated CodeMeta Concept: *isMaintainer*

### isRightsHolder
Context IRI: codemeta:isRightsHolder  
Type: xsd:boolean  
Subproperties: None  
Associated CodeMeta Concept: *isRightsHolder*

### issueTracker
Context IRI: codemeta:issueTracker  
Type: xsd:anyURI  
Subproperties: None  
Associated CodeMeta Concept: *IssueLink*

### licenseId
Context IRI: schema:license  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *License*

It is recommended that values for this property are selected from the Software Package Data Exchange
[list of licenses](http://spdx.org/licenses/), specifying a value listed in the "license identifier"
column, for example "Apache-2.0".

A copy of the SPDX v2.5 license list has been copied to the CodeMeta git repository, and exported from the source
Microsoft Excel file to Commma Separated Values as [spdx_licenselist_v2.5.csv](https://raw.githubusercontent.com/codemeta/codemeta/master/spdx_licenselist_v2.5.csv).

### name
Context IRI: schema:name  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *AgentName*

### packageSystem   
Context IRI: schema:packageSystem
Type: xsd:string
Subproperties: None
Parent property: dependencies

### programmingLanguage
Context IRI: schema:programmingLanguage  
Type: Not assigned  
Subproperties: name, version, URL  
Associated CodeMeta Concept: *ProgrammingLanguage*

Example:
```
    ...
    "programmingLanguage":{
      "name":"ruby",
      "version":"2.3.1",
      "URL":"https://www.ruby-lang.org/en/"
    }
    ...
```

### publisher
Context IRI: schema:publisher  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *Publisher*

### readme
Context IRI: codemeta:readme  
Type: xsd:anyURI  
Subproperties: None  
Associated CodeMeta Concept: *ReadmeLink*

### relatedIdentifier
Context IRI: codemeta:relatedIdentifier  
Type: xsd:string
Subproperties: None  
Parent property: *relationship*

### relatedIdentifierType
Context IRI: codemeta:relatedLink  
Type: xsd:string  
Subproperties: None  
Parent property: *relationship*

### relatedLink
Context IRI: codemeta:relatedLink  
Type: xsd:anyURI  
Subproperties: None  
Associated CodeMeta Concept: *RelatedLink*

### relatedPublications
Context IRI: codemeta:relatedPublications  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *RelatedPublications*

### relationship
Context IRI: codemeta:relationship  
Type: xsd:string  
Subproperties: *relationshipType*, *relatedIdentifier*, *relatedIdentifierType*  
Associated CodeMeta Concept: *Relationship*


The *relationship* property can be used to document a relationship between the software package
and another resource. The CodeMeta project recommends, but does not require, that the World Wide Web Consortium (W3C)
[PROV Data Model](http://www.w3.org/TR/prov-primer/) be used for expressing these relationships, when possible.

Some possible relationships from the PROV model include:
- [wasRevisionOf](http://www.w3.org/TR/prov-o/#wasRevisionOf)
- [hadMember](http://www.w3.org/TR/prov-o/#hadMember)
- [specializationOf](http://www.w3.org/TR/prov-o/#specializationOf)
- [wasInvalidatedBy](http://www.w3.org/TR/prov-o/#wasInvalidatedBy)

See [PROV Entity](http://www.w3.org/TR/prov-o/#Entity) for additional relationship types and examples.

This example shows the usage of the PROV [wasRevisionOf](http://www.w3.org/TR/prov-o/#wasRevisionOf) relationship,
which asserts that the software being described is a revised version of the software identifier by `relatedIdentifier`,
for example, the current software is a newer revision of the previous software:
```
...
"relationships": {
        "relationshipType": "wasRevisionOf",
        "namespace": "http://www.w3.org/ns/prov#",
        "relatedIdentifier": "urn:uuid:F1A0A7AF-ECF3-4C7D-B675-7C6949963995",
        "relatedIdentifierType": "UUID"
}
...
```

### relationshipType
Context IRI: codemeta:relationship  
Type: xsd:string  
Subproperties: None  
Parent property: *relationship*


some possible values for *relatedIdentifierType*:

```
ARK, arXiv, bibcode, DOI, EAN13, EISSN, ISBN, ISSN, ISTC, LISSN, LSID, PMID,
PURL, UPC, URL, URN
```

The following example instance file fragment indicates that the software package being
described has a component that has the Digital Object Identifier *doi:10.5063/F1VM496BXYZ*.
```

### role
Context IRI: codemeta:role   
Type: @id  
Subproperties: *namespace*, *roleCode*  
Associated CodeMeta Concept: *Role*

A function or part performed by an agent.

Example:
```
"role":[
   {
      "namespace":"http://www.ngdc.noaa.gov/metadata/published/xsd/schema/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
      "roleCode":[
         "originator",
         "resourceProvider"
      ]
   }
]
```

### roleCode
Context IRI: codemeta:roldCode  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *roleCode*  

The identifier that defines a specific function or part performed by a person or institution.

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
Associated CodeMeta Concept: *SoftwareCitation*

### identifier
Context IRI: dcterms:identifier  
Type: xsd:anyURI  
Subproperties: None  
Associated CodeMeta Concept: *SoftwareIdentifier*

### softwarePaperCitation
Context IRI: codemeta:softwarePaperCitation  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *SoftwarePaperCitation*

### title
Context IRI: dcterms:title  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *SoftwareTitle*

### @type
Context IRI: dc:type  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *ObjectType*

### suggests
Context IRI: schema:suggests  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *Suggests*

### tags
Context IRI: schema:keywords  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *Tags*

### testCoverage
Context IRI: codemeta:testCoverage  
Type: xsd:integer  
Subproperties: None  
Associated CodeMeta Concept: *TestCoverage*

### uploadedBy
Context IRI: codemeta:uploadedBy  
Type: Not specified  
Subproperties: *@id*, *email*, *name*  
Associated CodeMeta Concept: *UploadedBy*

### version
Context IRI: schema:version  
Type: xsd:string  
Subproperties: None  
Associated CodeMeta Concept: *Version*

### zippedCode
Context IRI: codemeta:zippedCode  
Type: xsd:anyURI  
Subproperties: None  
Associated CodeMeta Concept: *ZippedCodeLink*

## Appendix C Example Description File

The following JSON-LD document was created to describe the [*dataone* R package]( https://cran.r-project.org/web/packages/dataone/index.html ).

```
{
   "@context":"https://raw.githubusercontent.com/codemeta/codemeta/master/codemeta.jsonld",
   "@type":"SoftwareSourceCode",
   "agents":[
      {
         "@id":"http://orcid.org/0000-0003-0077-4738",
         "@type":"person",
         "email":"jones@nceas.ucsb.edu",
         "name":"Matt Jones",
         "affiliation":"NCEAS",
         "mustBeCited":true,
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
         "mustBeCited":true,
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
   "dependencies":
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
   "funding":"National Science Foundation grant #012345678",
   "isAutomatedBuild":false,
   "issueTracker":"https://github.com/DataONEorg/rdataone/issues",
   "licenseId":"Apache-2.0",
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
   "programmingLanguage":{
      "name":"R",
      "version":"> 3.1.1",
      "URL":"https://www.r-project.org"
   },
   "readme":"https://github.com/DataONEorg/rdataone/README.md",
   "issueTracker":"https://github.com/codemeta/codemeta/issues"
   "relatedPublications":"ISBN:0201703726",
   "relationship":{
       "relationshipType":"isPartOf",
       "relatedIdentifier":"urn:uuid:F1A0A7AF-ECF3-4C7D-B675-7C6949963995",
       "relatedIdentifierType":"UUID"
   },
   "softwareCitation":"Jones M, Slaughter P, Nahf R, Jones C, Boettiger C, Walker L, Hallett L, Chamberlain S, Hart E and Read J (2016). _redland: R Interface to the DataONE REST API_. doi: 10.5063/F1M61H5X (URL: http://doi.org/10.5063/F1M61H5X), R package version 2.0.0, <URL: http://github.com/DataONEorg/rdataone>.",
   "suggests":"No other software is suggested",
   "softwarePaperCitationIdentifiers":[
     "http://doi.org/0000/0000"
   ],
   "zippedCode":"https://cran.r-project.org/src/contrib/dataone_2.0.0.tar.gz"
}
```
