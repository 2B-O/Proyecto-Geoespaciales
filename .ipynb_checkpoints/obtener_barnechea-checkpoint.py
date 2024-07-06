import geopandas as gpd

def barnechea():
    """
    A partir de un archivo del censo de la comuna de lo barnechea, en la que hay manzanas urbanas,
    se crea un nuevo geodataframe de un solo poligono de las manzanas.
    """
    data = gpd.read_file("Datos/R13/MANZANA_IND_C17.shp")
    lo_barnechea = data[data.NOM_COMUNA == "LO BARNECHEA"]
    gdf = gpd.GeoDataFrame(geometry=[lo_barnechea.unary_union], crs=lo_barnechea.crs)
    gdf["NOM_COMUNA"] = "LO BARNECHEA"
    gdf = gdf[["NOM_COMUNA", "geometry"]]
    gdf.to_file("lo_barnechea.gpkg", driver="GPKG")
