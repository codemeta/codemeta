import csv
from pathlib import Path


REPO_DIR = Path(__file__).parent.parent


PROP_DESC_PATH = REPO_DIR / "properties_description.csv"
"""The CSV file where the leftmost columns of the aggregate crosswalk table
are (parent type, property name, type, and description."""

SOURCE_DIR = REPO_DIR / "crosswalks"
"""The directories where all other .csv files are."""

DEST_FILENAME = REPO_DIR / "crosswalk.csv"
"""The path/name of the file where the aggregate crosswalk table is
written."""


def check_property_names_match(filename, properties1, properties2):
    """Checks the list of properties in properties1 is the same as in
    properties2. Exits with a human-readable error if they don't."""
    if len(properties1) != len(properties2):
        print('Error in {}: expected {} properties, found {}. The aggregate '
              'table can only be built if every crosswalk lists exactly the '
              'properties in properties_description.csv, in the same order.'
              .format(filename, len(properties1) - 1, len(properties2) - 1))
        exit(1)
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
    with open(SOURCE_DIR / filename) as fd:
        rows = list(csv.reader(fd))

    # Some tables end with notes about terms of the other vocabulary that have
    # no CodeMeta equivalent. They have an empty first cell, are not part of
    # the crosswalk, and cannot be aggregated; skip them explicitly.
    rows = [row for row in rows if row and row[0]]

    # Split the two rows of the translation table.
    (codemeta_names, crosswalk_names) = columns_from_rows(rows)

    # Check the names match, in order to avoid messing the aggregate
    # table if there was a mistake in this table.
    check_property_names_match(filename, prop_desc[1], codemeta_names)

    return crosswalk_names

def list_crosswalks():
    """Returns the list of crosswalk files by auto-discovering them from the
    crosswalk/ directory."""
    return sorted(SOURCE_DIR.glob("*.csv"))

def aggregate():
    """Get all columns from properties_description.csv and files in
    crosswalks/, and concatenates them; returning a list of columns."""

    # Get the three left-most columns from properties_description.csv
    with open(PROP_DESC_PATH) as fd:
        prop_desc = columns_from_rows(csv.reader(fd))

    # Get the other columns, one per .csv file in crosswalks/
    columns = []
    for filename in list_crosswalks():
        columns.append(read_terms(prop_desc, filename))

    return prop_desc + columns

def write_aggregate(aggregate_columns):
    """Writes the aggregated crosswalk table."""
    rows = rows_from_columns(aggregate_columns)
    DEST_FILENAME.unlink(missing_ok=True)
    with open(DEST_FILENAME, 'a') as fd:
        writer = csv.writer(fd, lineterminator='\n')
        writer.writerows(rows)

def main():
    """Entry-point of the script."""
    write_aggregate(aggregate())

if __name__ == '__main__':
    main()
