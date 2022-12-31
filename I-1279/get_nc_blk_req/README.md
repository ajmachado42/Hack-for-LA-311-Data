# How to use this program:
---

Download this entire folder if you need Census block and NC geometry datasets.

1. Have the following handy: 
> - Your 311 Request API CSV (from [get_311_request_data_csv.py](https://github.com/hackforla/311-data/blob/dev/server/utils/get_request_data_csv.py)) filepath
> - Your Neighborhood Council shape file (.shp) filepath (folder is located in this repo; do not modify the folder)
> - Your Census blocks shape file (.shp) filepath (folder is located in this repo; do not modify the folder)
> - The Neighborhood Council name you are looking for. Make sure it matches the format and names found in the API csv file.
2. Open your terminal and navigate to the directory you want the final CSV to be saved in
3. Enter in the command line: python get_nc_blk.py
4. Follow the prompts for input of each file path
5. You may have to wait a bit for the program to fully execute
6. A confirmation will appear in your terminal when the program is complete

You will need the following packages:
- pandas
- geopandas
- shapely
- titlecase

If you encounter an issue with geopandas, "conda uninstall geopandas" then "conda install -c conda-forge geopandas" to make sure the right versions of each package are available. 