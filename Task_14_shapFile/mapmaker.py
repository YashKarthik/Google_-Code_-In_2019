import geopandas as gp

shpfile = gp.GeoDataFrame.from_file('shpfile.pbf')
shpfile.plot()