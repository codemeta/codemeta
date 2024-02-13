# CodeMeta

[![Join the chat at https://gitter.im/codemeta/codemeta](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/codemeta/codemeta?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Permanent Identifier](https://img.shields.io/badge/perma--id-https%3A%2F%2Fw3id.org%2Fcodemeta%2F3.0-blue.svg)](https://w3id.org/codemeta/3.0)

[CodeMeta](https://codemeta.github.io) [contributors](CONTRIBUTORS.MD) are creating a minimal metadata schema for science software and code, in JSON and XML. The goal of CodeMeta is to create a concept vocabulary that can be used to standardize the exchange of software metadata across repositories and organizations. CodeMeta started by comparing the software metadata used across multiple repositories, which resulted in the [CodeMeta Metadata Crosswalk](https://github.com/codemeta/codemeta/blob/master/crosswalk.csv).  That crosswalk was then used to generate a set of software metadata concepts, which were arranged into a JSON-LD context for serialization.

See <https://codemeta.github.io> for a visualization of the [crosswalk table](https://codemeta.github.io/crosswalk) and guides for [users](https://codemeta.github.io/user-guide/) and [developers](https://codemeta.github.io/developer-guide/).

## CodeMeta Schema

The schema for released versions of CodeMeta are:

- CodeMeta-3.0: [https://w3id.org/codemeta/v3.0](https://w3id.org/codemeta/v3.0)
    - *Matthew B. Jones, Carl Boettiger, Abby Cabunoc Mayes, Arfon Smith,  Morane Gruenpeter, Valentin Lorentz, Thomas Morrell, Daniel Garijo, Peter Slaughter, Kyle Niemeyer, Yolanda Gil, Martin Fenner, Krzysztof Nowak, Mark Hahnel, Luke Coy, Alice Allen, Mercè Crosas, Ashley Sands, Neil Chue Hong, Patricia Cruse, Daniel S. Katz, Carole Goble, Bryce Mecum, Alejandra Gonzalez-Beltran, Noam Ross.* 2023. __CodeMeta: an exchange schema for software metadata. Version 3.0.__ [https://w3id.org/codemeta/v3.0](https://w3id.org/codemeta/v3.0)
- CodeMeta-2.0: [https://doi.org/10.5063/schema/codemeta-2.0](https://doi.org/10.5063/schema/codemeta-2.0)
    - *Matthew B. Jones, Carl Boettiger, Abby Cabunoc Mayes, Arfon Smith, Peter Slaughter, Kyle Niemeyer, Yolanda Gil, Martin Fenner, Krzysztof Nowak, Mark Hahnel, Luke Coy, Alice Allen, Mercè Crosas, Ashley Sands, Neil Chue Hong, Patricia Cruse, Daniel S. Katz, Carole Goble.* 2017. __CodeMeta: an exchange schema for software metadata. Version 2.0.__ KNB Data Repository. [doi:10.5063/schema/codemeta-2.0](https://doi.org/10.5063/schema/codemeta-2.0)
- CodeMeta-1.0: [https://doi.org/10.5063/schema/codemeta-1.0](https://doi.org/10.5063/schema/codemeta-1.0)
    - *Matthew B. Jones, Carl Boettiger, Abby Cabunoc Mayes, Arfon Smith, Peter Slaughter, Kyle Niemeyer, Yolanda Gil, Martin Fenner, Krzysztof Nowak, Mark Hahnel, Luke Coy, Alice Allen, Mercè Crosas, Ashley Sands, Neil Chue Hong, Patricia Cruse, Daniel S. Katz, Carole Goble.* 2016. __CodeMeta: an exchange schema for software metadata.__ KNB Data Repository. [doi:10.5063/schema/codemeta-1.0](https://doi.org/10.5063/schema/codemeta-1.0)

## Contributors

CodeMeta is a community project with many contributors spanning research, education, and engineering domains.    - See our [list of Contributors](CONTRIBUTORS.MD). You can cite the CodeMeta schema and project as:

> *Matthew B. Jones, Carl Boettiger, Abby Cabunoc Mayes, Arfon Smith,  Morane Gruenpeter, Valentin Lorentz, Thomas Morrell, Daniel Garijo, Peter Slaughter, Kyle Niemeyer, Yolanda Gil, Martin Fenner, Krzysztof Nowak, Mark Hahnel, Luke Coy, Alice Allen, Mercè Crosas, Ashley Sands, Neil Chue Hong, Patricia Cruse, Daniel S. Katz, Carole Goble, Bryce Mecum, Alejandra Gonzalez-Beltran, Noam Ross.* 2023. __CodeMeta: an exchange schema for software metadata. Version 3.0.__ [https://w3id.org/codemeta/v3.0](https://w3id.org/codemeta/v3.0)

## How you can help

Join us!  We welcome help formalizing a schema and creating mappings between existing software metadata schemas and the proposed schema. And writing documentation. And evangelizing. And other stuff, however you might be able to contribute.

- Send us a pull request if you have any updates to our [schema](https://github.com/codemeta/codemeta/blob/master/codemeta.jsonld) or [mappings](https://github.com/codemeta/codemeta/tree/master/crosswalks/)! See the [contribution guide](https://github.com/codemeta/codemeta/blob/master/CONTRIBUTING.md).
- Take a look at the [issue tracker](https://github.com/codemeta/codemeta/issues)
- Join the discussion!
    - [Join the CodeMeta chat gitter.im](https://gitter.im/codemeta/codemeta) (May not always be active, best to ping us directly in the GitHub issues if you don't get a response).

## Project history

This is an extension of the work done by [@arfon](http://github.com/arfon/), [@hubgit](https://github.com/hubgit/), [@kaythaney](https://github.com/kaythaney/) and others on [Code as a Research Object](https://github.com/mozillascience/code-research-object) / [fidgit](https://github.com/mozillascience/fidgit). __Code as a research object__ is a [Mozilla Science Lab](http://mozillascience.org) ([@MozillaScience](https://github.com/mozillascience/)) project working with community members to explore how we can better integrate code and scientific software into the scholarly workflow. Out of this came __fidgit__ - a proof of concept integration between GitHub and figshare, providing a [Digital Object Identifier](http://en.wikipedia.org/wiki/Digital_object_identifier) (DOI) for the code which allows for persistent reference linking.

With codemeta, we want to formalize the schema used to map between the different services (GitHub, figshare, Zenodo) to help others plug into existing systems. Having a standard software metadata interoperability schema will allow other data archivers and libraries join in. This will help keep science on the web shareable and interoperable!

## Organizers

The CodeMeta project has a [governance model](https://codemeta.github.io/governance/) and 
a [governing body](https://codemeta.github.io/governance/people/) to oversee the development and maintenance of the CodeMeta vocabulary, 
crosswalk table, website, software and other related content.

## Links

- __Code as a Research Object__ blog posts:
    - [Code as a research object: updates, prototypes, next steps](http://mozillascience.org/code-as-a-research-object-updates-prototypes-next-steps/)
    - [What else is needed for code reuse](http://mozillascience.org/what-else-is-needed-for-code-reuse/)
    - [JSON-LD for software discovery, reuse and credit](http://www.arfon.org/json-ld-for-software-discovery-reuse-and-credit)
- [JSON-LD.org](http://json-ld.org/)
- [Schema.org](http://schema.org/)
