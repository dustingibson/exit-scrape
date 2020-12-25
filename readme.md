# Usage:



## Save NYT Polling Data

Save NYT files. This required to do before grabbing data.

`python scrape.py get`

## Get Data

`python scrape.py data "keyword"`


Keyword represents the keyword on the table.

e.g.

`python scrape.py data "Under $25,000"`

This produces states.csv file with all necessary data.

## Save SVG

Will read the produced data.csv and saves anewmap.svg file

`python to_svg.py`