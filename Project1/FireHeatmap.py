
import folium
from folium.plugins import HeatMap
import pandas as pd

df = pd.read_csv("FireData23.csv", low_memory=False)
df = df.dropna(subset=['Latitude', 'Longitude'])

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=6)

heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]
HeatMap(heat_data, radius=10).add_to(m)

m.save('fire_heatmap.html')
