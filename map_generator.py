"""
Create an interactive web map from a CSV file of location data.
"""

import pandas as pd
import folium


def load_location_data(csv_path):
    """
    Load location data from a CSV file.

    Parameters:
        csv_path (str): Path to the input CSV file.

    Returns:
        pandas.DataFrame: Table containing location names, latitudes, and longitudes.
    """
    return pd.read_csv(csv_path)


def create_location_map(data):
    """
    Create an interactive Folium map using latitude and longitude values.

    Parameters:
        data (pandas.DataFrame): Location data with name, latitude, and longitude columns.

    Returns:
        folium.Map: Interactive map containing location markers.
    """
    centre_latitude = data["latitude"].mean()
    centre_longitude = data["longitude"].mean()

    location_map = folium.Map(
        location=[centre_latitude, centre_longitude],
        zoom_start=7
    )

    for _, row in data.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row["name"]
        ).add_to(location_map)

    return location_map


def save_map(location_map, output_path):
    """
    Save the interactive map as an HTML file.

    Parameters:
        location_map (folium.Map): The map to save.
        output_path (str): Path for the output HTML file.
    """
    location_map.save(output_path)


if __name__ == "__main__":
    locations = load_location_data("sample_locations.csv")
    map_object = create_location_map(locations)
    save_map(map_object, "output_map.html")

    print("Map created successfully: output_map.html")