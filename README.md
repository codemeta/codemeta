CodeMeta
========
[![Join the chat at https://gitter.im/codemeta/codemeta](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/codemeta/codemeta?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/codemeta/codemeta.svg?branch=master)](https://travis-ci.org/codemeta/codemeta)

[CodeMeta](https://codemeta.github.io) is creating minimal metadata schemas for science software and code, in JSON and XML.

This is an extension of the work done by [@arfon](http://github.com/arfon/), [@hubgit](https://github.com/hubgit/), [@kaythaney](https://github.com/kaythaney/) and others on [Code as a Research Object](https://github.com/mozillascience/code-research-object) / [fidgit](https://github.com/mozillascience/fidgit). **Code as a research object** is a [Mozilla Science Lab](http://mozillascience.org) ([@MozillaScience](https://github.com/mozillascience/)) project working with community members to explore how we can better integrate code and scientific software into the scholarly workflow. Out of this came **fidgit** - a proof of concept integration between Github and figshare, providing a [Digital Object Identifier](http://en.wikipedia.org/wiki/Digital_object_identifier) (DOI) for the code which allows for persistent reference linking.

With codemeta, we want to formalize the schema used to map between the different services (Github, figshare, Zenodo) to help others plug into existing systems. Having a standard software metadata interoperability schema will allow other data archivers and libraries join in. This will help keep science on the web shareable and interoperable!

JSON-LD schema: https://github.com/codemeta/codemeta/blob/master/codemeta.jsonld

Example instance: https://github.com/codemeta/codemeta/blob/master/examples/example-codemeta-full.json

Comparison of current APIs in this space: https://github.com/codemeta/codemeta/blob/master/crosswalk.csv

[FAQ](../blob/master/docs/faq.md)


How you can help
================

We need help formalizing a schema and creating mappings between existing software metadata schemas and the proposed schema.

* Send us a pull request if you have any updates to our [schema](https://github.com/codemeta/codemeta/blob/master/codemeta.jsonld) or [mappings](https://github.com/codemeta/codemeta/blob/master/codemeta-crosswalk.md)!
* Take a look at the [issue tracker](https://github.com/codemeta/codemeta/issues)
* Join the discussion!
    * [(JSON-LD) Metadata for software discovery](https://github.com/mozillascience/code-research-object/issues/15)
    * [How should software be cited?](https://github.com/mozillascience/code-research-object/issues/12)
    * [What information is needed to reuse code?](https://github.com/mozillascience/code-research-object/issues/2)


Organizers
==========

* Matt Jones
* Arfon Smith
* Abby Cabunoc Mayes
* Carl Boettiger

Links
=====

* **Code as a Research Object** blog posts:
    * [Code as a research object: updates, prototypes, next steps](http://mozillascience.org/code-as-a-research-object-updates-prototypes-next-steps/)
    * [What else is needed for code reuse](http://mozillascience.org/what-else-is-needed-for-code-reuse/)
    * [JSON-LD for software discovery, reuse and credit](http://www.arfon.org/json-ld-for-software-discovery-reuse-and-credit)

* [JSON-LD.org](http://json-ld.org/)
* [Schema.org](http://schema.org/)
