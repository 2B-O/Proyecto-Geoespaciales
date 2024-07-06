import geopandas as gpd
import os

def barnechea():
    """
    A partir de un archivo del censo de la comuna de lo barnechea, en la que hay manzanas urbanas,
    se crea un nuevo geodataframe de un solo poligono de las manzanas.
    """
    print("Obteniendo la comuna de Lo Barnechea...")
    ruta = os.path.join("Datos", "LO_BARNECHEA", "lo_barnechea.gpkg")
    if os.path.exists(ruta):
        # el archivo ya existente
        os.remove(ruta)
    else:
        print("El archivo no fue borrado...")
    data = gpd.read_file("Datos/R13/MANZANA_IND_C17.shp")
    lo_barnechea = data[data.NOM_COMUNA == "LO BARNECHEA"]
    gdf = gpd.GeoDataFrame(geometry=[lo_barnechea.unary_union], crs=lo_barnechea.crs)
    gdf["NOM_COMUNA"] = "LO BARNECHEA"
    gdf = gdf[["NOM_COMUNA", "geometry"]]
    gdf.loc[0, "geometry"] = gdf.convex_hull.geometry[0]

    # Guardar el archivo
    gdf.to_file(ruta, driver="GPKG")
