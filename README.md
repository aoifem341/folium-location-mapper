# Folium Location Mapper

A Python-based workflow for visualising geographic point data as interactive web maps using Folium.

## Project Description

This project reads location data from a CSV file containing place names, latitudes, and longitudes. The script uses the Folium library to create an interactive web map with markers for each location and exports the result as an HTML file that can be viewed in any web browser.

## Dependencies

The project requires the following Python packages:

* Python
* Folium
* Pandas

Additional packages used within the project environment are listed in `environment.yml`.

## Installation

Clone the repository:

```bash
git clone https://github.com/aoifem341/folium-location-mapper.git
```

Create the project environment:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate folium-location-mapper
```

## Input Data

The script requires a CSV file containing the following columns:

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

Run the script from the repository directory:

```bash
python map_generator.py
```

## Output

The script creates an interactive HTML file:

```text
output_map.html
```

This file can be opened in any web browser to display the generated map and interact with the location markers.

## Repository Structure

```text
folium-location-mapper/
├── map_generator.py
├── sample_locations.csv
├── environment.yml
├── README.md
├── LICENSE
└── output_map.html
```

