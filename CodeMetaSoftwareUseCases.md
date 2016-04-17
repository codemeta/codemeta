Edited Use cases
CodeMeta meeting in Portland
Created 20160415 (use cases group pulled from here 230pm 20160516) https://docs.google.com/document/d/1SalOP_tLw7FC6jnoz5hJBB2jA7xBClKqc88wgmJu5Ro/edit






The “six” Use Case categories: from Matt and Carl’s slide summary 20160417
* Facilitate citation
* Enable credit, compliance, and quality
* Facilitate discovery and access
* Understand software functionality
* Enable interoperability
* Enable transparency and reproducibility




THE ‘ORIGINAL’ 13 CASES: 20160415
Then determine a final set of categorized use cases based on these 3 different sets


1. Identify software functionality
   * Overall
   * Module level
   * Function level
   * Identify functional equivalency with other {modules, functions, etc)
1. Understand dependencies
   * Identify Installation Dependencies (User)
   * Identify Development/Build Dependencies (Developer)
   * Use dependencies to enable transitive credit
   * Automate build processes
   * Identify dependencies to assign (aspects of? partial?) credit
   * Understand role of software in an application (even if we cannot access or install)
1. Facilitate Discovery
   * Support discovery for reuse
   * Discover tools that can perform a specific function
      * Enable comparisons of tool functionality
   * Classify and find tools by domain, and other controlled vocabularies
   * Locate tools that were used for particular applications/results
   * Discover location of software
1. Enable credit, compliance, and evaluation
   * Identify roles of software contributors
      * Authors
      * Metadata authors
      * Curators
      * Other roles (see publisher’s credit ontology)
   * Document compliance with funders policies
   * Identify funder of software
1. Citation
   * Cite software product generally
   * Cite a specific software version/release
   * Cite a software paper describing the software
   * Provide sufficient info for formal citation in the reference list (authors, title, repository, publication year)
   * Link to a landing page with more detailed information about the software
   * Link to the source code
1. Count the citations to a given version of software
   * For acknowledgement/credit
   * As a quality metric for discovery
* Aggregate by person, by infrastructure, etc.
1. Enable Interoperability
   * Describe platform, language constraints
   * Describe input-output formats
   * Describe input-output semantics
   * Enable pipeline building
   * Describe constraints on parameters
   * Identify license obligations
1. Describe provenance information
   * Execution parameters, limitations / assumptions
1. Enable transparency and reproducibility (via dependencies and source linkages)
2. Communicate permissions / License terms
3. Identify software status (See http://www.repostatus.org)
   * Build status
   * Maintenance status
   * Understand intention of software publication (compliance, reuse, etc.)
   * …
1. Motivate archiving of software
2. Evaluate software quality


















Codemeta Meeting Portland, Edited Use cases, Working Document                        1
Day 2, PM 20160416 : Carole Goble, Alice Allen, Ashley Sands, Patricia Cruse
Edited Use cases
Created 20160415 (use cases group pulled from here 3pm 20160516)
CodeMeta meeting in Portland
This document is the electronic version of the “whiteboarding” we did in the workshop






	Stakeholder
	Utility Infrastructure
	Indexers
	Developer
	Repository Mgr.
	Researcher
	Funder
	Publisher
	Citation Mgr
	Library / Curator
	Action*
	

	

	

	

	

	

	

	

	

	

	Deposit**
	

	

	

	

	

	

	

	

	

	

	Discover: 3, 4
	

	

	

	

	

	

	

	

	

	

	Analyse: 1, 2, 6, 9, 11
	

	

	

	

	

	

	

	

	

	

	Use
	

	

	

	

	

	

	

	

	

	

	C3R: 4, 5, 6
	

	

	

	

	

	

	

	

	

	

	

TO DO:
*add subpoints to each action
**add concepts (by #) under stakeholder for each relevant action sub-point










  







Stakeholder list pulled from SCWG:
https://github.com/force11/force11-scwg/blob/master/sc-principles/software-citation-principles.tex



Stakeholders: Digital Repositories, Publishers, Information Science, Indexers, Software Developers,


datacite/crossref/orcid -- utility providers


`Researcher'' includes both academic researchers (e.g., postdoc, tenure-track faculty member) and research software engineers. \item


``Publisher'' includes both traditional publishers that publish text and\slash or software papers as well as archives such as Zenodo that directly publish software. \item


``Funder'' is a group that funds software or work using software. \item


``Indexer'' examples include Scopus, Web of Science, Google Scholar, and Microsoft Academic Search. \item `


`Domain group\slash library\slash archive'' includes the Astronomy Source Code Library (ASCL)~\cite{ascl}, bioCADDIE~\cite{bioCADDIE}, Computational Infrastructure for Geodynamics (CIG)~\cite{CIG}, libraries, institutional archives, etc. \item


``Repository'' refers to public software repositories such as GitHub, Netlib, Comprehensive R Archive Network (CRAN), and institutional repositories. \item `


``Citation manager`` refers to people and organizations that create scholarly reference management software and websites including Zotero, Mendeley, EndNote, RefWorks, BibDesk, etc., that manage citation information and semi-automatically insert those citations into research products.