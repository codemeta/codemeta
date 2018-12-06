# Contribution Guide

This guide is intended for people who want to contribute to content of the Git repository.

## Layout

The repository is laid out as such:

* `scripts/`: Python scripts to manipulate the crosswalk table
* `properties_description.csv`: A CSV files with human-readable information about each CodeMeta property.
* `crosswalks/*.csv`: Two-column CSV files, that map between CodeMeta's properties and platform-specific terms.
* `crosswalk.csv`: An aggregated table of all CSV files mentionned above; intended to be the main resource for readers.

## About pull requests

Do not commit changes to `crosswalk.csv`, as these will very likely create conflicts with other pull requests, and make either these PRs or yours unmergeable.

`crosswalk.csv` will be updated by repository maintainers when appropriate.

## Editing an existing mapping

Open the CSV file in `crosswalks/` that contains your mapping.
You may change the second column (ie. what comes after the comma on each line) to match the terms of the platform your new mapping covers.

Then, run `scripts/aggregate.py`. This will build the new `crosswalk.csv` using the updated version of your mapping; and raise an error if you made a mistake (such as editing the first column).

You can now commit your changes and send a pull request. Don't forget to **exclude** `crosswalk.csv` from the commit.

## Contributing a new mapping

To add a new platform mapping to CodeMeta, you have to add a new CSV file to `crosswalks/`. The filename is free-form, but please to avoid non-ASCII characters. The name is not used to build the aggregated table.

You may copy any other CSV file from `crosswalks/` to write yours; the refer to the "Editing an existing mapping" section.

## Adding a new CodeMeta property

To do so, you should first edit `properties_description.csv` and add a line with the appropriate cells there; and edit `codemeta.jsonld` as well.

Then, add that line to each `crosswalks/*.csv` file, in the same position as in `properties_description.csv`.

Then, run `scripts/aggregate.py`. This will build the new `crosswalk.csv` with the new property; and raise an error if you made a mistake (such as editing the first column).

You may then create a commit and send a pull request. Don't forget to **exclude** `crosswalk.csv` from the commit.
