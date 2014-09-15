codemeta
========

Minimal metadata schemas for science software and code, in JSON and XML.

This is an extention of the work done by @arfon, @hubgit, @kaythaney and others on [Code as a Research Object](https://github.com/mozillascience/code-research-object) / [fidgit](https://github.com/mozillascience/fidgit). **Code as a research object** is a [Mozilla Science Lab](http://mozillascience.org) (@MozillaScience) project working with community members to explore how we can better integrate code and scientific software into the scholarly workflow. Out of this came **fidgit** - a bridge between Github and figshare, providing a [Digital Object Identifier](http://en.wikipedia.org/wiki/Digital_object_identifier) (DOI) for the code which allows for persistent reference linking.

In codemeta, we want to formalize the schema used to map between the different services (Github, figshare, Zenodo) to help others plug in to this existing system. Having a standard schema will help other data archivers and libraries join in. This will help keep the science on the web shareable and interoperable.

JSON-LD schema: https://github.com/mbjones/codemeta/blob/master/codemeta.jsonld
Crosswalk table: https://github.com/mbjones/codemeta/blob/master/codemeta-crosswalk.md
