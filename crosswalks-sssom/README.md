# Mapping-methodology

- **Version**: 0.0.1
- **Authors**: Esteban Gonzalez, Daniel Garijo, Morane Gruenpeter, SciCodes working group
- **Date**: 01-04-2025

This repository contains the instructions to create new crosswalks between Codemeta and another specification or vocabulary, as well as some examples of the generation. We rely on the SSSOM standard to create a machine-readable mapping representation, with some extensions.

The methodology for generating the files required to create the crosswalk is as follows:
1. **Identify the Terms to Map**
   Identify the terms you want to map in both semantic artifacts (source and codemeta term). 
2. **Create a YAML Metadata File**
   Create a YAML metadata file that contains the metadata of the mapping using the provided template in the template folder: mapping-template.yml.
   Name the file appropriately, for example, codemeta-bibtext-mapping.yml.
3. **Complete the Required Metadata Fields**<br>
   - mapping_date: The date when the mapping was created (use ISO 8601 format).
   - mapping_set_description: A description of the mapping, including references to the involved domains and the purpose of the mapping.
   - mapping_provider: Information about the entity responsible for the mapping. Include a URI if possible.
   - mapping_set_id: The URI of the mapping (see next step). Consider using persistent identifiers instead of standard URLs. A persistent identifier can be minted using the w3id.org project. Please, add it in the project codemeta/crosswalks
   - subject_source: The URL of the specification or vocabulary. Use persistent identifiers whenever possible.
4. **Create the Data File (CSV Format)**
   Name the CSV file appropriately, for example, `codemeta-bibtext-mapping.csv`.
   The CSV file should contain the following columns:
   - source_term: The corresponding term in the source specification or vocabulary. If the term is part of a parent concept, please, include it by using the entire path. For example, the term name in datacite is a property of the concep creators (use creators/name in the column)
   - codemeta_term: The term in CodeMeta.If the term is part of a parent concept, please, include it by using the entire path. For example, the term name in codemeta belongs to the concept author (use author/name in the column)
   - type_relation: The type of relation between the two terms. Possible values:
       - exact_match: The terms are equivalent concepts.
       - part_of: The source concept is part of the codemeta concept (e.g., a publication date in the source vocabulary is part of a publication year in the codemeta vocabulary ).
       - more_specific_than: the source vocabulary term the codemeta term is more specific than the codemeta term. For example, "hal_id more_specific_than codemeta:identifier" means that the hal id is a more concrete term than the "identifier" property in CodeMeta. 
       - more_generic_than:  The source vocabulary term is more generic than the CodeMeta term. For example, " status more_generic_than codemeta:developmentStatus" means that the status is a more generic term than the "developmentStatus" property in CodeMeta.
       - close_match: The subject and the object are sufficiently similar that they can be used interchangeably in some information retrieval applications. For example, if the source and codemeta properties refer to dates, but the format is different.
   - combined_mapping: **It applies ONLY to a part-of relationship**.
     This column defines the formula used to combine terms between schemas.
     For example, if the CodeMeta vocabulary has the term `date`, and the source vocabulary has the terms `year` and `month`, the combined_mapping should be as follows: $(year) + $(month)`.
   - comments: additional (optional) annotations about the mapping itself.

5. **Generate the SSSOM File**<br>
   **Note:** This script uses the library sssom. Please, install it before executing the script.
   ```bash
   pip install sssom
   ```
   Execute the script (generate_crosswalk.py) to generate an .sssom.tsv file from the CSV.
   ```bash
   python ./generate_crosswalk.py examples/bibtex-codemeta-mappings.yaml examples/bibtex-codemeta-mappings.csv
   ```
### FAQ
Below we have collected frequently asked questions 

#### How do I mint a persistent identifier for my mapping/crosswalk?
Create a folder with a unique name. The folder name will be used to create a unique identifier. No need to anything else!
The corresponding identifier will be `https://w3id.org/codemeta/mappings/{YOUR_ID}`, where `{YOUR_ID}` is the id of your mapping.

For example, for the `bibtex` mapping, the corresponding identifier is [https://w3id.org/codemeta/mappings/bibtex](https://w3id.org/codemeta/mappings/bibtex).
#### How do I fill in the crosswalk table? What does "more specific" and "more general" means?
The crosswalks indicate term relationships between two schemas.  The `source_term` is is the term from the mapped schema. The `codemeta_term` is the term from CodeMeta`.
The `type_relation` indicates what type of relationship exist between those terms. We support several terms, please see point 4 above.

#### My metadata term maps to several properties in CodeMeta. How do I represent it?
If you have a term that mapps to more than one term in CodeMeta (or viceversa), please add a row per mapping. For example, in the [bibtex crosswalk](https://github.com/oeg-upm/codemeta/blob/crosswalks_oeg/crosswalks-sssom/bibtex/bibtex-codemeta-mappings.csv) we have the terms `hal_id` and `doi` which are mapped to CodeMeta term `identifier`.
In both cases `identifier` is more specific than `hal_id` and more specific than `doi`, since both `hal_id` and `doi` are types of identifiers, but not all identifiers are `dois` or `hal_ids`.

#### What if my specification has hierarchical concepts like authors.name?
In some cases, terms may have a structure as follows: `vocab.owner.name is an exact match to codemeta.author.name`
Here you will need to fill some extra columns with the path (parent term) in the mapping. Hierarchy will be delimited by the character '/'. For example:
      
      | source_term | codemeta_term | source_term_path | codemeta_term_path |
      | ----------- | ------------- | ---------------- | ------------------ |
      | owner/name  | author/name   | owner            | author             |


#### My metadata term is a composite of another term. How do I represent it?
If you have a codemeta term that can be composed as a combination of 2 or more terms in your vocabulary, you can use the `part_of` relationship for the mapping, and the `combined_mapping` column to specify how both terms are combined. See for example the [bibtex crosswalk](https://github.com/oeg-upm/codemeta/blob/crosswalks_oeg/crosswalks-sssom/bibtex/bibtex-codemeta-mappings.csv), which combines `month` and `year` into `datePublished`.

### What happens if the format used by the term is different? ###

Apparently, we need to represent two types of relationships. Let's look at an example: Format (DataCite) and programmingLanguage (CodeMeta). Format is more generic than programmingLanguage, but the formats also differ—DataCite uses MIME types, while programmingLanguage may be expressed as plain text. How can we represent this situation?

In this case, our recommendation is to include the relationship defined by this methodology (more_generic_than) in the 'type of relation' column, and to add a reference to the format in the 'comments' column.

### What happens if the cardinality of the source is different than in the object? ###

There are cases where the cardinality of the source term differs from that of the object term. For example, in DataCite, the term 'formats' is a list of formats, while in CodeMeta, we have the term 'fileFormat.'. In these cases, we recommend adding a row with the mapping and providing a comment to emphasize this difference. 

### Final considerations
Some of the strategies defined in this methodology are not directly applicable in SSSOM (e.g., formula representation). However, we consider this information  key when reading a crosswalk, and therefore we propose to document it.
