import folium
from folium.plugins import HeatMap
import pandas as pd

# Load the fire data CSV into a pandas DataFrame
df = pd.read_csv('FireData.csv')

# Create a base map centered around Oregon
m = folium.Map(location=[44.0, -120.0], zoom_start=7)

# Extract latitude and longitude from the dataframe
fire_locations = df[['Lat_DD', 'Long_DD']].dropna()

# Prepare the data for the heatmap (latitude, longitude)
heat_data = [[row['Lat_DD'], row['Long_DD']] for index, row in fire_locations.iterrows()]

# Add the heatmap layer to the map
HeatMap(heat_data).add_to(m)

# Save the map to an HTML file
m.save('oregon_fire_heatmap.html')
