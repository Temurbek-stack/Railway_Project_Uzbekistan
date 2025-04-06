from google.colab import drive
drive.mount('/content/drive')

from folium.plugins import GroupedLayerControl, MarkerCluster
from folium import Map, PolyLine, CircleMarker, FeatureGroup, LayerControl, IFrame
import geopandas as gpd
import pandas as pd
import numpy as np
import folium


%run '/content/drive/MyDrive/UTY/UTY/Python code/AUX_mtu_correction.ipynb'
%run '/content/drive/MyDrive/UTY/UTY/Python code/AUX_electrification.ipynb'

neighboring_countries_railways = gpd.read_file("/content/drive/MyDrive/UTY/UTY/3. qgis project/neighbors/railways_cleaned/neighboring_railways_cleaned.shp")
neighboring_countries_stations = gpd.read_file("/content/drive/MyDrive/UTY/UTY/3. qgis project/neighbors/stations/stations_neigboring_countries_shp.gpkg")
neighboring_countries_stations = gpd.GeoDataFrame(neighboring_countries_stations)

railway_metro_stations_joined = gpd.read_file("/content/drive/MyDrive/UTY/UTY/Python code/railway_metro_stations_joined/railway_metro_stations_joined.shp")
railway_station_names_final = pd.read_excel("/content/drive/MyDrive/UTY/UTY/Python code/railway_station_names_final.xlsx")

# Assuming the function get_color is to be used later in the code
def get_color(new_station_type):
    if pd.isna(new_station_type):
        return "gray"
    return {
        "Yuk tashishga oid": "black",
        "Oraliqdagi": "#0066CC",
        "Uchastkadagi": "#00994C",
        "Saralovchi": "orange",
        "Yoʻlovchi tashishga oid": "red"
    }.get(new_station_type, "gray")


colors_list = {
    "Yuk tashishga oid": "black",
    "Oraliqdagi": "#0066CC",
    "Uchastkadagi": "#00994C",
    "Saralovchi": "orange",
    "Yoʻlovchi tashishga oid": "red"
}


def get_color_mtu(MTU):
    return {
        "Tashkent": "#0000FF",
        "Kokand": "#FF00FF",
        "Bukhara": "#FF8000",
        "Karshi": "#00CC66",
        "Termez": "#0080FF",
        "Kungirat": "#7F00FF"}.get(MTU, "#000000")

colors_list_mtu = {
    "Tashkent": "#0000FF",
    "Kokand": "#FF00FF",
    "Bukhara": "#FF8000",
    "Karshi": "#00CC66",
    "Termez": "#0080FF",
    "Kungirat": "#7F00FF"}


# Create a base map
m = folium.Map(location=[41, 64.5853], zoom_start=6.2, tiles='OpenStreetMap')

# Function to create label content
def create_label(row):
    return f"""<strong>{row['station_name']}</strong><br>Type: {row['new_station_type']}<br>Class: {row['station_class']}<br>MTU: {row['MTU']}"""


layers = {
    "Bo‘luvchi punkt": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='color: gray; font-size: 18px;'>\u25A0</div><div style='margin-left: 5px;'>Bo‘luvchi punkt</div></div>"),
    "Oraliqdagi": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='color: #0066CC; font-size: 18px;'>\u25A0</div><div style='margin-left: 5px;'>Oraliqdagi</div></div>"),
    "Saralovchi": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='color: orange; font-size: 18px;'>\u25A0</div><div style='margin-left: 5px;'>Saralovchi</div></div>"),
    "Uchastkadagi": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='color: #00994C; font-size: 18px;'>\u25A0</div><div style='margin-left: 5px;'>Uchastkadagi</div></div>"),
    "Yoʻlovchi tashishga oid": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='color: red; font-size: 18px;'>\u25A0</div><div style='margin-left: 5px;'>Yoʻlovchi tashishga oid</div></div>"),
    "Yuk tashishga oid": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='color: black; font-size: 18px;'>\u25A0</div><div style='margin-left: 5px;'>Yuk tashishga oid</div></div>"),
    "Kungirat": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='background-color: #7F00FF; width: 10px; height: 2px;'></div><div style='margin-left: 5px;'>Kungirat</div></div>"),
    "Bukhara": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='background-color: #FF8000; width: 10px; height: 2px;'></div><div style='margin-left: 5px;'>Bukhara</div></div>"),
    "Karshi": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='background-color: #00CC66; width: 10px; height: 2px;'></div><div style='margin-left: 5px;'>Karshi</div></div>"),
    "Termez": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='background-color: #0080FF; width: 10px; height: 2px;'></div><div style='margin-left: 5px;'>Termez</div></div>"),
    "Tashkent": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='background-color: #0000FF; width: 10px; height: 2px;'></div><div style='margin-left: 5px;'>Tashkent</div></div>"),
    "Kokand": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='background-color: #FF00FF; width: 10px; height: 2px;'></div><div style='margin-left: 5px;'>Kokand</div></div>"),
    "Electrified": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='background-color: red; width: 10px; height: 2px;'></div><div style='margin-left: 5px;'>Electrified</div></div>"),
    "Not Electrified": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='background-color: gray; width: 10px; height: 2px;'></div><div style='margin-left: 5px;'>Not Electrified</div></div>"),
    "Railway Tracks": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='background-color: purple; width: 10px; height: 2px;'></div><div style='margin-left: 5px;'>Railway Tracks</div></div>"),
    "Railway Stations": folium.FeatureGroup(name="<div style='display: inline-flex; align-items: center;'><div style='color: #6666FF; font-size: 18px;'>\u25A0</div><div style='margin-left: 5px;'>Railway Stations</div></div>"),
}

# Iterate over unique station types
for station_type, subset_data in railway_station_names_final.groupby('new_station_type'):
    # Generate label content
    label_content = ['<strong>{}</strong><br>Type:{}<br>Class:{}<br>MTU:{}'.format(row['station_name'], row['new_station_type'], row['station_class'], row['MTU']) for _, row in subset_data.iterrows()]

    for name, value in layers.items():
        if name == station_type:
            for index, (label, row) in enumerate(zip(label_content, subset_data.iterrows())):
                _, row = row
                folium.CircleMarker(
                    location=[row['lat'], row['lng']],
                    color=get_color(station_type),
                    radius=2.5 if station_type != "Oraliqdagi" else 0.7,
                    fill=True,
                    fill_opacity=1,
                    popup=folium.Popup(IFrame(label, width=200, height=100), max_width=200),
                    ).add_to(layers[name])


railways_by_MTUs = railways_by_MTUs.to_crs('EPSG:4326')
unique_MTUs = railways_by_MTUs['MTU'].unique()


for mtu1 in unique_MTUs:
    subset_data_mtu = railways_by_MTUs[railways_by_MTUs['MTU'] == mtu1]

    all_coordinates = []

    # Iterate over each LineString geometry and extract its coordinates
    for _,row in subset_data_mtu.iterrows():
        # Extract coordinates for the current LineString
        coordinates = [[coord[1], coord[0]] for coord in row['geometry'].coords]
        # Append the coordinates to the list
        all_coordinates.append(coordinates)

    for name, value in layers.items():
        if name==mtu1:
            folium.PolyLine(locations = all_coordinates,
            color= get_color_mtu(mtu1),
            weight=3,
            opacity=1,
            ).add_to(layers[name])


electrified_yes_sf = electrified_yes_sf.to_crs('EPSG: 4326')

locations_for_elec_yes = []

    # Iterate over each LineString geometry and extract its coordinates
for geom in electrified_yes_sf.geometry:
    # Extract coordinates as a list of tuples (x, y)
    if geom is not None:
        # Extract coordinates as a list of tuples (x, y)
        coords = [[coord[1], coord[0]] for coord in geom.coords]
        # Append coordinates to the locations list
        locations_for_elec_yes.append(coords)

folium.PolyLine(locations=locations_for_elec_yes,
                     color="red",
                     weight=2.5,
                     opacity=0.5).add_to(layers['Electrified'])

electrified_no_sf = electrified_no_sf.to_crs('EPSG:4326')

locations_for_elec_no = []

    # Iterate over each LineString geometry and extract its coordinates
for geom in electrified_no_sf.geometry:
    # Extract coordinates as a list of tuples (x, y)
    if geom is not None:
        # Extract coordinates as a list of tuples (x, y)
        coords = [[coord[1], coord[0]] for coord in geom.coords]
        # Append coordinates to the locations list
        locations_for_elec_no.append(coords)

folium.PolyLine(locations=locations_for_elec_no,
                     color="gray",
                     weight=2.5,
                     opacity=0.5).add_to(layers['Not Electrified'])

neighboring_countries_railways = neighboring_countries_railways.to_crs('EPSG:4326')

locations_for_n_c_railways = []

    # Iterate over each LineString geometry and extract its coordinates
for geom in neighboring_countries_railways.geometry:
    # Extract coordinates as a list of tuples (x, y)
     if geom is not None:
        # Extract coordinates as a list of tuples (x, y)
        coords = [[coord[1], coord[0]] for coord in geom.coords]
        # Append coordinates to the locations list
        locations_for_n_c_railways.append(coords)

folium.PolyLine(locations=locations_for_n_c_railways,
                     color="purple",
                     weight=1.5,
                     opacity=0.7).add_to(layers['Railway Tracks'])


neighboring_countries_stations = neighboring_countries_stations.to_crs('EPSG: 4326')
neighboring_countries_stations['lng'] = neighboring_countries_stations.geometry.x
neighboring_countries_stations['lat'] = neighboring_countries_stations.geometry.y


for idx, row in neighboring_countries_stations.iterrows():
    folium.CircleMarker(location=[row['lat'], row['lng']],
                        color="#3186cc",
                        radius=0.3,
                        fill=True,
                        fill_opacity=0.5,
                        popup=row['name']).add_to(layers['Railway Stations'])


for layer in layers.values():
    layer.add_to(m)

default = {
        layers["Kungirat"]: True,
        layers["Bukhara"]: True,
        layers["Karshi"]:True,
        layers["Termez"]:True,
        layers["Tashkent"]:True,
        layers["Kokand"]:True,
        layers["Bo‘luvchi punkt"]:True,
        layers["Oraliqdagi"]:True,
        layers["Saralovchi"]:True,
        layers["Uchastkadagi"]:True,
        layers["Yoʻlovchi tashishga oid"]:True,
        layers["Yuk tashishga oid"]:True,
        layers["Railway Stations"]: False,
        layers["Railway Tracks"]: False,
        layers["Electrified"]: False,
        layers["Not Electrified"]: False
    }


GroupedLayerControl(
    groups={
        'Regional Railway Junctions': [
            layers["Kungirat"],
            layers["Bukhara"],
            layers["Karshi"],
            layers["Termez"],
            layers["Tashkent"],
            layers["Kokand"]],
        'Railway Stations by Types': [
            layers["Bo‘luvchi punkt"],
            layers["Oraliqdagi"],
            layers["Saralovchi"],
            layers["Uchastkadagi"],
            layers["Yoʻlovchi tashishga oid"],
            layers["Yuk tashishga oid"]],
        'Neighbor Countries': [
            layers["Railway Stations"],
            layers["Railway Tracks"]],
        'Electrification': [
            layers["Electrified"],
            layers["Not Electrified"]]},
    exclusive_groups=False,
    collapsed= False,
).add_to(m)

m

m.save('/content/drive/MyDrive/UTY/UTY/Python code/map_with_electrification.html')