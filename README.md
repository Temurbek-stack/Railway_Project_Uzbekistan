# 🚆 Railway Infrastructure Mapping – Uzbekistan

## 🗺️ Overview

**Railway_Project_Uzbekistan** is a comprehensive geospatial project aimed at **mapping the entire railway infrastructure of Uzbekistan**, including main lines, regional connections, and neighboring country links. It integrates data from **OpenStreetMap**, enriched with **electrification status**, **station classifications**, and **interactive visualizations** built using Python, R, and QGIS.

This project allows users to explore the railway landscape of Uzbekistan in a flexible, modular way — enabling **infrastructure planning**, **logistics optimization**, and **transportation research** through an intuitive, multi-layered map system.

> 📍 **Explore the Final Map**: See the interactive output in `final_outcome/Final_Outcome_OPENME.html`

---

## 📂 Project Structure

The repository is structured into key folders and notebooks, ensuring a clean workflow from **data acquisition** to **interactive visualization**:

### 📁 Directories

- `3.qgis_project/` – Core shapefiles (`.shp`, `.dbf`, etc.) used for the QGIS project and Python-based visualization  
- `4.other_shapefiles/` – Auxiliary shapefiles specifically focused on **railway electrification**, **station types**, and **track classification**

---

## 📒 Notebooks Included

This project is organized around **three Jupyter notebooks**, each playing a critical role in data preparation and map creation:

### 1. `AUX_electrification.ipynb`
- Processes and integrates **electrification status** of railway tracks
- Cleans and standardizes metadata fields for visual clarity

### 2. `AUX_mtu_correction.ipynb`
- Corrects and verifies data for **MTU** (Mintaqaviy Temir yo'l Uzellari – Regional Railway Junctions)
- Ensures accurate representation of key railway hubs

### 3. `MAIN_map.ipynb`
- Main notebook for **generating the final interactive railway map**
- Includes layer controls to toggle railway types, electrification, junctions, stations, and borders
- Saves output as an HTML file for offline access and sharing

> 💡 **Pro Tip**: Use layer toggles in the HTML map to visualize various infrastructure components independently.

---

## 🧹 Data Acquisition & Cleaning

For a detailed step-by-step breakdown of how the data was sourced, cleaned, and validated, refer to:

📄 `Data Acquisition and Cleaning.pdf`

### 🔍 Highlights:

- Data sourced from **OpenStreetMap** via `osmnx` and QGIS manual inspection
- Electrification data harmonized across segments and added as an attribute layer
- Station names and MTU locations manually cross-checked with official rail authority maps

---

## 🚀 How to Use This Project

To run this project via **Google Colab** and visualize the final railway map:

### ✅ Step 1: Copy to Google Drive
Clone or download this repository and move it to your **Google Drive** (e.g., `MyDrive/Railway_Project_Uzbekistan/`).

### ✅ Step 2: Mount Google Drive in Colab
Each notebook includes code to mount your Drive. Make sure to run that cell first.


```python
from google.colab import drive
drive.mount('/content/drive')


### ✅ Step 3: Run `MAIN_map.ipynb`
This notebook generates the **final HTML map** showing Uzbekistan’s full railway infrastructure. You'll be able to:

- View main lines vs regional lines
- Toggle electrified vs non-electrified routes
- See MTUs and rail stations separately
- Save the interactive map to your Drive as a shareable `.html` file

## 🌐 Technologies & Tools Used

- **Python**: `geopandas`, `folium`, `osmnx`, `shapely`, `matplotlib`
- **QGIS**: Spatial preprocessing, layer styling  
- **Jupyter Notebooks**: Data cleaning, processing, visualization logic  
- **OpenStreetMap**: Primary geodata source

---

## 🧠 Skills Demonstrated

This project highlights your ability to:

- 🗺️ **Perform geospatial analysis** using both Python and QGIS  
- 🧹 **Conduct thorough data cleaning and validation**  
- 🚦 **Integrate transportation-specific metadata** (e.g., electrification, MTU, stations)  
- 🧩 **Work with complex shapefile structures and attribute joins**  
- 🌐 **Build and export interactive web-based maps from Python**  
- 📦 **Package large geospatial datasets into a clean, reproducible format**  
- 📊 **Create insightful data visualizations** of infrastructure and network elements

---

## 📝 Final Notes

This platform is designed for urban planners, railway engineers, researchers, and students who are interested in understanding the structure of Uzbekistan’s railway network in depth.

It balances automation with manual validation, enabling high accuracy while maintaining reproducibility.  
The combination of open geodata, code-based workflows, and GIS tools makes this a scalable foundation for **future transport modeling and planning initiatives**.
