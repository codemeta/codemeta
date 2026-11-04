import csv
import re
from pathlib import Path


REPO_DIR = Path(__file__).parent.parent


PROP_DESC_PATH = REPO_DIR / "properties_description.csv"
"""The CSV file where the leftmost columns of the aggregate crosswalk table
are (parent type, property name, type, and description."""

SOURCE_DIR = REPO_DIR / "crosswalks"
"""The directories where all other .csv files are."""

CROSSWALK_PATH = REPO_DIR / "crosswalk.csv"
"""The path/name of the file where the aggregate crosswalk table is
written."""


with open(CROSSWALK_PATH) as fd:
    reader = csv.reader(fd)
    lines = list(reader)
cols = list(zip(*lines))
props = cols[1]
for col in cols[4:]:
    col_name = col[0]
    # Windows does not allow these characters in file names. A run of them
    # becomes one "-", so "CPAN::Meta" gives "CPAN-Meta".
    safe_name = re.sub(r'[<>:"/\\|?*]+', '-', col_name)
    filename = SOURCE_DIR / f"{safe_name}.csv"
    filename.unlink(missing_ok=True)
    with open(filename, 'a') as fd:
        writer = csv.writer(fd)
        for (prop, trans) in zip(props, col):
            writer.writerow((prop, trans))

PROP_DESC_PATH.unlink(missing_ok=True)
with open(PROP_DESC_PATH, 'a') as fd:
    writer = csv.writer(fd, lineterminator='\n')
    prop_desc = zip(*cols[0:4])
    for row in prop_desc:
        writer.writerow(row)
