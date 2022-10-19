# Hack for LA - [311 Data Project](https://www.hackforla.org/projects/311-data.html) - [I-1279](https://github.com/hackforla/311-data/issues/1279) - Analyzing hotspots for 311 Requests
---
Identify addresses or small areas that could benefit from more signage, increased community assistance, or other actions related to 311

# Data Descriptions
---

| Filename/Folder | Type | Description |
| --------------- | ---- | ----------- |
| 01_00_nc_api_cleaning | .ipynb | API dataset pulled from 10/01/21-10/01/22 cleaned |
| 01_01_nc_eda | .ipynb | Exploration of 311 requests by Neighborhood Council - all requests, addresses w/ >= 2 requests, addresses w/ >= 5 requests, timeseries by NC |
| 01_02_block_eda | .ipynb | Exploration of requests by block created in 02_00_geospatial_cleaning |
| 02_00_geospatial_cleaning | .ipynb | Cleaning of geodata for Neighborhood Council and 2020 Census block boundaries; spatial merge w/ NC and block boundaries; spatial merge w/ 311 request address point geometry and block geometries | 
| 02_01_nc_only_viz | .ipynb | Folium choropleth map with 311 request data by Neighborhood Council; layered choropleth map by type by Neighborhood Council; addresses dropped that did not have a certified NC |
| 02_02_block_only_viz | .ipynb | Folium choropleth map with all 311 request data by Census block; addresses dropped that did not have a matching census block |
| 02_03_nc_blk_viz | .ipynb | Folium choropleth map with all 311 Request data by Neighborhood Council and Census block; Census blocks use  quantile bins for the legend |
| get_311_request_data_csv | .py | [get_311_request_data_csv.py](https://github.com/hackforla/311-data/blob/dev/server/utils/get_request_data_csv.py) for timeframe API pulls; replace datetime, as necessary; cmd line - python get_311_request_data_csv.py "2021-10-01" "2022-10-01" |
| images | folder | Various charts from EDAs |
| streamlit | folder | Contains .py file for streamlit app and .html files of Folium maps used in streamlit |
