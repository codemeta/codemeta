#!/usr/bin/env python3
import os
import csv

REPO_DIR = os.path.join(os.path.dirname(__file__), '..')

PROP_DESC_PATH = os.path.join(REPO_DIR, 'properties_description.csv')
"""The CSV file where the leftmost columns of the aggregate crosswalk table
are (parent type, property name, type, and description."""

SOURCE_DIR = os.path.join(REPO_DIR, 'crosswalks')
"""The directories where all other .csv files are."""

DEST_FILENAME = os.path.join(REPO_DIR, 'crosswalk.csv')
"""The path/name of the file where the aggregate crosswalk table is
written."""

OLD_ORDER = [
    'codemeta-V1.csv',
    'DataCite.csv',
    'OntoSoft.csv',
    'Zenodo.csv',
    'GitHub.csv',
    'Figshare.csv',
    'Software Ontology.csv',
    'Software Discovery Index.csv',
    'Dublin Core.csv',
    'R Package Description.csv',
    'Debian Package.csv',
    'Python Distutils (PyPI).csv',
    'Python PKG-INFO.csv',
    'Trove Software Map.csv',
    'Perl Module Description (CPAN::Meta).csv',
    'NodeJS.csv',
    'Java (Maven).csv',
    'Octave.csv',
    'Ruby Gem.csv',
    'ASCL.csv',
    'DOAP.csv',
    'Wikidata.csv',
    'Citation File Format Core (CFF-Core) 1.0.2.csv',
    ]

USE_OLD_ORDER = True
"""Set this to False to auto-discover files in the crosswalk/ directory."""

def check_property_names_match(filename, properties1, properties2):
    """Checks the list of properties in properties1 is the same as in
    properties2. Exits with a human-readable error if they don't."""
    for (prop1, prop2) in zip(properties1, properties2):
        if prop1 != prop2:
            print('Error in {}: property names {} and {} should be the same'
                  .format(filename, prop1, prop2))
            exit(1)

def columns_from_rows(rows):
    """from a list of rows, returns a list of columns."""
    return list(zip(*rows))

def rows_from_columns(cols):
    """from a list of columns, returns a list of rows."""
    return list(zip(*cols))

def read_terms(prop_desc, filename):
    """Reads the crosswalk of one of the mappings, checks its integrity,
    and returns its list of terms, in the same order as the ones
    in properties_description.csv."""

    # Read rows from a translation table in crosswalks.
    with open(os.path.join(SOURCE_DIR, filename)) as fd:
        rows = list(csv.reader(fd))

    # Split the two rows of the translation table.
    (codemeta_names, crosswalk_names) = columns_from_rows(rows)

    # Check the names match, in order to avoid messing the aggregate
    # table if there was a mistake in this table.
    check_property_names_match(filename, prop_desc[1], codemeta_names)

    return crosswalk_names

def list_crosswalks():
    """Returns the list of crosswalk files. If USE_OLD_ORDER, returns
    OLD_ORDER. Otherwise, auto-discovers them from the crosswalk/
    directory."""
    if USE_OLD_ORDER:
        return OLD_ORDER
    else:
        return sorted(os.listdir(SOURCE_DIR))

def aggregate():
    """Get all columns from properties_description.csv and files in
    crosswalks/, and concatenates them; returning a list of columns."""

    # Get the three left-most columns from properties_description.csv
    with open(PROP_DESC_PATH) as fd:
        prop_desc = columns_from_rows(csv.reader(fd))

    # Get the other columns, one per .csv file in crosswalks/
    columns = []
    for filename in list_crosswalks():
        if filename.endswith('.csv'):
            columns.append(read_terms(prop_desc, filename))

    return prop_desc + columns

def rm_file(filename):
    """Removes a file if it exists, does nothing otherwise."""
    try:
        os.unlink(filename)
    except FileNotFoundError:
        pass

def write_aggregate(aggregate_columns):
    """Writes the aggregated crosswalk table."""
    rows = rows_from_columns(aggregate_columns)
    rm_file(DEST_FILENAME)
    with open(DEST_FILENAME, 'a') as fd:
        writer = csv.writer(fd, lineterminator='\n')
        writer.writerows(rows)

def main():
    """Entry-point of the script."""
    write_aggregate(aggregate())

if __name__ == '__main__':
    main()
