classes:  
  
Version  
Specification  
Repository  
	SVNRepository  
	BKRepository  
	GitRepository  
	CVSRepository  
	ArchRepository  
	BazaarBranch  
	HgRepository  
	DarcsRepository  
  
(not clear that classes ma meaningfully)  
  
Properties:  
  
name 		- schema:name  
homepage 	- schema:url  
old-homepage 	- schema:relatedLink  
created 	- schema:dateCreated  
shortdesc	- schema:title  
description	- schema:description  
release		- schema:version  
mailing-list	-   
category	- schema:keyword  
license		- schema:license  
repository	- schema:codeRepository  
anon-root	- (schema:codeRepository)  
browse		- (schema:codeRepository)  
module		- (CVS/Arch/BK repo thing)  
location	- (repository location)  
download-page	- schema:downloadUrl  
download-mirror - ditto?  
revision	- identifier of a revision; codemeta:relatedIdentifier or schema:version?  (property of Version type)  
file-release	- (property of doap:Version type)  
wiki		-   
bug-database	- issuesTracker  
screenshots	- schema:screenshot (not explicitly in codemeta)  
maintainer	- codemeta:maintainer  
developer	- schema:contributor  
documenter	- schema:contributor  
translator	- schema:contributor  
tester		- schema:contributor  
helper		- schema:contributor  
programming-language	- schema:programmingLanguage  
os			- schema:operatingSystem  
implements  
service-endpoint  
language		- schema:programmingLanguage  
vendor		- schema:publisher  
platform	- schema:runtimePlatform (not explicitly in codemeta)  
audience  
blog		- schema:relatedLink  
   
