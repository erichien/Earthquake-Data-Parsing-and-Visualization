import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot
from config import Config


def plot_geopandas(data, place):
    """
    Plot all earthquakes that happened at the given place in the past month on a map with geopandas.
    """

    location, location_code = place, Config.STATE_CODES[place]

    # import geojson file and store as GeoPandas DataFrame
    gdf = gpd.read_file(Config.FILEPATH)
    # keep columns relevant to output
    gdf = gdf[['place', 'mag', 'geometry']]
    # find earthquake records of the given location using state name and abbreviation
    gdf_local = gdf[gdf['place'].str.contains('{}|{}'.format(location, location_code))]

    # load United States geo data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    usa = world[world['name'] == 'United States']

    (fig, ax) = plt.subplots(figsize=(10,10))
    ax.set_aspect('equal')
    usa.plot(ax=ax, color='chartreuse', edgecolor='grey')
    # plot earthquake data on map, with color intensity representing their magnitude
    gdf_local.plot(ax=ax, column='mag', cmap='OrRd', markersize=5)
    plt.show()


def plot_plotly(data, place):
    """
    Plot all earthquakes that happened at the given place in the past month on a map with plotly.
    """

    mapbox_access_token = 'pk.eyJ1IjoieW91Z29lcmljIiwiYSI6ImNqZ2R4cmpsbTI3dzcycXFzdHRrdnFobGUifQ.xwe3ccbSH-QrCY9WPoYJ2w'
    location, location_code = place, Config.STATE_CODES[place]

    df = pd.io.json.json_normalize(data['features'])
    # keep columns relevant to output
    df = df[['properties.place', 'properties.mag', 'geometry.coordinates']]
    # find earthquake records of the given location using state name and abbreviation
    df_local = df[df['properties.place'].str.contains('{}|{}'.format(location, location_code))]
    df_local = df_local.rename(index=str, columns={'properties.place': 'place', 'properties.mag': 'mag'})
    df_local['long'] = df_local['geometry.coordinates'].apply(lambda x: x[0])
    df_local['lat'] = df_local['geometry.coordinates'].apply(lambda x: x[1])
    df_local = df_local.drop(['geometry.coordinates'], axis=1)

    site_lat = df_local.lat
    site_lon = df_local.long
    locations_name = df_local.place
    scale = [ [0, "rgb(255, 160, 30)"], [1, "rgb(200, 0, 0)"] ]

    data_local = Data([
                Scattermapbox(
                    lat = site_lat,
                    lon = site_lon,
                    mode = 'markers',
                    marker = Marker(
                            size = 14,
                            color = df_local['mag'],
                            colorscale = scale,
                            cmin = df_local['mag'].min(),
                            cmax = df_local['mag'].max(),
                            opacity = 0.8,
                            colorbar=dict(
                                title="Magnitude"
                                )
                            ),
                    ),
                Scattermapbox(
                    lat = site_lat,
                    lon = site_lon,
                    mode = 'markers',
                    marker = Marker(
                        size = 6,
                        color = 'rgb(240, 200, 170)',
                        opacity = 0.5
                    ),
                )]
            )

    layout = Layout(
            title = 'Earthquake In the Past Month',
            autosize = True,
            hovermode = 'closest',
            showlegend = False,
            mapbox = dict(
                    accesstoken = mapbox_access_token,
                    bearing = 0,
                    center = dict(
                            lat=38,
                            lon=-98
                    ),
            pitch = 0,
            zoom = 3,
            style = 'outdoors'
            ),
        )

    fig = dict(data=data_local, layout=layout)
    plot(fig, filename='EarthquakeDataInThePastMonth.html')
