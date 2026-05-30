# Folium Location Mapper

A Python-based workflow for visualising geographic point data as interactive web maps using Folium.

## Installation

Clone the repository:

```bash
git clone https://github.com/aoifem341/folium-location-mapper.git
```

Create the environment:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate egm722
```

## Input Data

The script requires a CSV file containing:

* name
* latitude
* longitude

Example:

```csv
name,latitude,longitude
Exeter,50.7184,-3.5339
Plymouth,50.3755,-4.1427
```

## Running the Script

```bash
python map_generator.py
```

## Output

The script creates:

```text
output_map.html
```

which can be opened in a web browser to display an interactive map.
