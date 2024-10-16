import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


shapefile_path = "./srprec_state_p20_v01_shp/srprec_state_p20_v01_shp.shp"
gdf = gpd.read_file(shapefile_path)
print(gdf.head(20))
print(gdf.info())

gdf.plot("COUNTY", edgecolor="black", linewidth=0.1)  
plt.show()