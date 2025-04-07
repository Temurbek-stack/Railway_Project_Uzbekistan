🚆 Railway Infrastructure Mapping – Uzbekistan

🗘️ Overview
# Railway_Project_Uzbekistan
A comprehensive repository for mapping Uzbekistan's railway infrastructure. Includes data acquisition from OpenStreetMap, detailed validation and cleaning steps, electrification status integration, and interactive visualizations using Python, R, and QGIS.

**Overview**

This project is focused on mapping the railway network of the Republic of Uzbekistan, including regional and neighboring railways and stations. It utilizes Python for data manipulation and presentation. The project structure includes essential shapefiles for map creation, auxiliary notebooks for preprocessing data, and a main notebook for generating the final map visualization. See the 'Final_Outcome_OPENME.html' file in final_outcome folder for the final interactive map of Uzbekistan Railways. 

**Project Structure**

- 3.qgis project: This directory contains shapefiles (.shp) essential for working with the map.
- 4.other_shapefiles: Here, you'll find additional shapefiles specific to railways, including data on electrification status.

**Notebooks** 

The project includes three main Jupyter notebooks:
- AUX_electrification: Processes electrification data for railways.
- AUX_mtu_correction: Applies corrections to MTU (Regional Railway Junctions - Mintaqaviy Temir yo’l Uzeli) data.
- MAIN_map: Generates the final map visualization of the Uzbekistan railway network. This notebook allows for interactive layer selection to view different parts of the map separately.

See Data Acquisition and Cleaning.pdf file for detailed data acquisition and cleaning processes.

**Usage Instructions**

To use this project, follow these steps:
1. Download the Google Drive Repository: Initially, download the project repository to your own Google Drive under MyDrive for easy access and manipulation.
2. Mount Google Colab to Google Drive: Instructions for this are included in each notebook. This step is essential for accessing and processing the project files.
3. Run the MAIN_map Notebook: Once Google Drive is mounted, you can execute the MAIN_map notebook to generate and view the railway map.
Additionally, the MAIN_map notebook includes functionality to save the resulting map as an HTML file in the Python Code directory on your Drive. This facilitates easy access to the map without the need to run other notebooks.

**Final Notes**

This project is designed for ease of use, allowing for detailed visualization of Uzbekistan's railway network with
the flexibility to explore specific layers and features. The included notebooks ensure that all necessary data
preprocessing and map generation steps are comprehensible and executable within a Google Colab
environment.
