#!/usr/bin/env python3

import os
import csv
from pprint import pprint


REPO_DIR = os.path.join(os.path.dirname(__file__), '..')

PROP_DESC_PATH = os.path.join(REPO_DIR, 'properties_description.csv')
"""The CSV file where the leftmost columns of the aggregate crosswalk table
are (parent type, property name, type, and description."""

SOURCE_DIR = os.path.join(REPO_DIR, 'crosswalks')
"""The directories where all other .csv files are."""

CROSSWALK_PATH = os.path.join(REPO_DIR, 'crosswalk.csv')
"""The path/name of the file where the aggregate crosswalk table is
written."""


def rm_file(filename):
    """Removes a file if it exists, does nothing otherwise."""
    try:
        os.unlink(filename)
    except FileNotFoundError:
        pass

with open(CROSSWALK_PATH) as fd:
    reader = csv.reader(fd)
    lines = list(reader)
cols = list(zip(*lines))
props = cols[1]
for col in cols[4:]:
    col_name = col[0]
    filename = os.path.join(SOURCE_DIR, col_name + '.csv')
    rm_file(filename)
    with open(filename, 'a') as fd:
        writer = csv.writer(fd)
        for (prop, trans) in zip(props, col):
            writer.writerow((prop, trans))

rm_file(PROP_DESC_PATH)
with open(PROP_DESC_PATH, 'a') as fd:
    writer = csv.writer(fd, lineterminator='\n')
    prop_desc = zip(*cols[0:4])
    for row in prop_desc:
        writer.writerow(row)
