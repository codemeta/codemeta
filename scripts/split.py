#!/usr/bin/env python3

import os
import csv
from pprint import pprint

def rm_file(filename):
    """Removes a file if it exists, does nothing otherwise."""
    try:
        os.unlink(filename)
    except FileNotFoundError:
        pass

with open('crosswalk.csv') as fd:
    reader = csv.reader(fd)
    lines = list(reader)
cols = list(zip(*lines))
props = cols[1]
for col in cols[4:]:
    col_name = col[0]
    filename = os.path.join('crosswalks', col_name + '.csv')
    rm_file(filename)
    with open(filename, 'a') as fd:
        writer = csv.writer(fd)
        for (prop, trans) in zip(props, col):
            writer.writerow((prop, trans))

rm_file('properties_description.csv')
with open('properties_description.csv', 'a') as fd:
    writer = csv.writer(fd, lineterminator='\n')
    prop_desc = zip(*cols[0:4])
    for row in prop_desc:
        writer.writerow(row)
