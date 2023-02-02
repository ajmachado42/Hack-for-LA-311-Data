import streamlit as st
import streamlit.components.v1 as components

# https://github.com/randyzwitch/streamlit-folium
from streamlit_folium import st_folium

st.markdown("# City of Los Angeles 311 Request Data\n --- \n ### by Neighborhood Council & Block-by-Block")
st.markdown("[Adriana Machado's Github](https://github.com/ajmachado42/Hack-for-LA-311-Data/tree/master/I-1279) | [Hack for LA 311 Data Project](https://www.hackforla.org/projects/311-data.html)")
st.markdown("[Neighborhood Council Shapefile Source](https://data.lacity.org/City-Infrastructure-Service-Requests/Neighborhood-Councils-Certified-/fu65-dz2f) | [LA Blocks Census Shapefile Source](https://www2.census.gov/geo/tiger/TIGER2020PL/STATE/06_CALIFORNIA/06037/)")

# adapted from https://discuss.streamlit.io/t/include-an-existing-html-file-in-streamlit-app/5655/3
HtmlFile = open("nc_blk_layered.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 800, width = 1100)

# https://github.com/randyzwitch/streamlit-folium
# st_folium(HtmlFile)

# Folium Type x Block
HtmlFile2 = open("blk_type_layered.html", 'r', encoding='utf-8')
source_code2 = HtmlFile2.read() 
print(source_code2)
components.html(source_code2, height = 800, width = 1100)

# Folium Type x NC 
HtmlFile3 = open("nc_type_layered.html", 'r', encoding='utf-8')
source_code3 = HtmlFile3.read() 
print(source_code3)
components.html(source_code3, height = 800, width = 1100)