# DataONE Indexing of CodeMeta Documents

## Introduction

DataONE indexing will be updated to accept data from CodeMeta documents.

## Index Fields

The following table summarizes the data available from a CodeMeta document for insertion
into the DataONE Solr index, and the currently available fields in the index.

In some cases an existing DataONE field may be used to store the corresponding CodeMeta property,
such as for 'title'. Other CodeMeta properties will require new fields to be added to the Solr index.

| CodeMeta Property | DataONE Index Field | Index? | New Field? | Comment |
| ----------------- | --------------------| ------ | ---------- | ------- |
| agents/@id | | | | |
| agents/affiliation | | | | |
| agents/email | | | | |
| agents/isMaintainer | | | | |
| agents/isRightsHolder | | | | |
| agents/mustBeCited | | | | |
| agents/name | author |Y|N| when roleCode=originator |
| agents/role/namespace | | | | |
| agents/role/roleCode | | | | |
| buildInstructions | | | | |
| codeRepository | | | | |
| contIntegration | | | | |
| controlledTerms | keywords |Y|N| |
| dateCreated | | | | |
| dateModified | | | | |
| datePublished | dataUploaded |Y|N| Is this the correct usage for datePublished? |
| depends/identifier| | | | |
| depends/name | | | | |
| depends/operatingSystem | | | | |
| depends/packageSystem | | | | |
| depends/version| | | | |
| description | abstract |Y| | |
| developmentStatus | | | | |
| downloadLink | | | | |
| embargoDate | | | | |
| funding | | | | |
| identifier | id |Y|N| Can we use this, as the D1 id has a restricted format? |
| isAutomatedBuild | | | | |
| issueTracker | | | | |
| licenseId | | | | |
| operatingSystems | | | | |
| packageSystem | | | | |
| programmingLanguage/name | | | | |
| programmingLanguage/version | | | | |
| programmingLanguage/URL | | | | |
| publisher | | | | |
| readme | | | | |
| relationships/relatedIdentifier | | | | |
| relationships/relatedIdentifierType | prov_wasDerivedFrom |Y|N| when relationshipType = wasDerivedFrom
| relationships/relationshipType | | | | |
| relatedLink | | | | |
| relatedPublications | | | | |
| suggests/identifier | | | | |
| suggests/name | | | | |
| suggests/operatingSystem | | | | |
| suggests/packageSystem | | | | |
| suggests/version | | | | |
| softwarePaperCitationIdentifiers | | | | |
| tags | topic or term |Y|N| which index field should be used?|
| title | title |Y|N| |
| version | | | | |
| uploadedBy/@id | | | | |
| uploadedBy/@type | | | | |
| uploadedBy/email | | | | |
| uploadedBy/name | | | | |
| uploadedBy | | | | |
| zippedCode | | | | |
| | attribute | | | |
| | attributeDescription | | | |
| | attributeLabel | | | |
| | attributeName | | | |
| | attributeUnit | | | |
| | authorGivenName | | | |
| | authoritativeMN | | | |
| | authorLastName | | | |
| | authorSurName | | | |
| | beginDate | | | |
| | blockedReplicationMN | | | |
| | changePermission | | | |
| | checksum | | | |
| | checksumAlgorithm | | | |
| | class | | | |
| | contactOrganization | | | |
| | datasource | | | |
| | dataUrl | | | |
| | dateModified | | | |
| | datePublished | | | |
| | dateUploaded | | | |
| | decade | | | |
| | documents | | | |
| | eastBoundCoord | | | |
| | edition | | | |
| | endDate | | | |
| | family | | | |
| | fileID | | | |
| | fileName | | | |
| | formatId | | | |
| | formatType | | | |
| | gcmdKeyword | | | |
| | genus | | | |
| | geoform | | | |
| | investigator | | | |
| | isDocumentedBy | | | |
| | isPublic | | | |
| | isService | | | |
| | isSpatial | | | |
| | keyConcept | | | |
| | kingdom | | | |
| | mediaType | | | |
| | mediaTypeProperty | | | |
| | namedLocation | | | |
| | noBoundingBox | | | |
| | northBoundCoord | | | |
| | numberReplicas | | | |
| | obsoletedBy | | | |
| | obsoletes | | | |
| | ogcUrl | | | |
| | order | | | |
| | origin | | | |
| | originator | | | |
| | parameter | | | |
| | phylum | | | |
| | placeKey | | | |
| | preferredReplicationMN | | | |
| | presentationCat | | | |
| | project | | | |
| | prov_generated | | | |
| | prov_generatedByExecution | | | |
| | prov_generatedByProgram | | | |
| | prov_generatedByUser | | | |
| | prov_hasDerivations | | | |
| | prov_hasSources | | | |
| | prov_instanceOfClass | | | |
| | prov_used | | | |
| | prov_usedByExecution | | | |
| | prov_usedByProgram | | | |
| | prov_usedByUser | | | |
| | prov_wasExecutedByExecution | | | |
| | prov_wasExecutedByUser | | | |
| | prov_wasInformedBy | | | |
| | pubDate | | | |
| | purpose | | | |
| | readPermission | | | |
| | relatedOrganizations | | | |
| | replicaMN | | | |
| | replicationAllowed | | | |
| | replicaVerifiedDate | | | |
| | resourceMap | | | |
| | rightsHolder | | | |
| | scientificName | | | |
| | sem_annotated_by | | | |
| | sem_annotates | | | |
| | sem_annotation | | | |
| | sem_comment | | | |
| | sensor | | | |
| | seriesId | | | |
| | serviceCoupling | | | |
| | serviceDescription | | | |
| | serviceEndpoint | | | |
| | serviceInput | | | |
| | serviceOutput | | | |
| | serviceTitle | | | |
| | serviceType | | | |
| | site | | | |
| | size | | | |
| | source | | | |
| | southBoundCoord | | | |
| | species | | | |
| | submitter | | | |
| | term | | | |
| | topic | | | |
| | updateDate | | | |
| | webUrl | | | |
| | westBoundCoord | | | |
| | writePermission | | | | |
