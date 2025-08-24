import pandas as pd
import geopandas as gpd
import re

emitters = pd.read_excel('data/epa_ghrp_emitters.xls', skiprows=6, header=0)
emitters_gdf = gpd.GeoDataFrame(emitters, 
                                  geometry=gpd.points_from_xy(emitters['LONGITUDE'], emitters['LATITUDE']),
                                  crs='EPSG:4326')

electronics_co_buyers = pd.read_excel('data/epa_ghrp_co_buyers_electronics_manufacturing.xls', skiprows=6, header=0)
electronics_co_buyers['SECTOR'] = 'Petrochemical Production' 
petrochem_co_buyers = pd.read_excel('data/epa_ghrp_co_buyers_petrochem_prod.xls', skiprows=6, header=0)
petrochem_co_buyers['SECTOR'] = 'Electronics Manufacturing' 

co_buyers = pd.concat([electronics_co_buyers, petrochem_co_buyers], ignore_index=True)
co_buyers_gdf = gpd.GeoDataFrame(co_buyers, 
                                  geometry=gpd.points_from_xy(co_buyers['LONGITUDE'], co_buyers['LATITUDE']),
                                  crs='EPSG:4326')

for df in [emitters_gdf, co_buyers_gdf]:
    df.columns = [re.sub(r'[\s()]', '_', c.lower()).replace("__", "_") for c in df.columns]
    df = df.rename(columns={"ghg_quantity__metric_tons_co2e_":"ghg_quantity_metric_tons_co2e"})