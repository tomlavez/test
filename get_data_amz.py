import geopandas as gpd

gdf = gpd.read_file('deter-amz-public-2025mai23/deter-amz-deter-public.shp')

gdf_sem_geom = gdf.drop(columns='geometry')

gdf_sem_geom.to_csv('deter_amz_dados.csv', index=False)

print("Arquivo CSV criado: deter_amz_dados.csv")