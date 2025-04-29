import pandas as pd
import plotly.express as px

import folium 
from folium.plugins import HeatMap

df = pd.read_csv("FireData.csv")

fig  = px.density_mapbox(df, lat = "Lat_DD", lon = "Long_DD", z = "EstTotalAcres", radius = 20, 
                         center=dict(lat=df.Lat_DD.mean(), lon = df.Long_DD.mean()),
                         zoom = 5.75, mapbox_style = 'open-street-map', height=900)

fig.show()