import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load the CSV data
df = pd.read_csv('LandSlide.csv')

# Filter out rows with missing coordinates
df = df.dropna(subset=['x', 'y'])

# Convert Web Mercator (EPSG:3857) to lat/lon (WGS84)
# This requires pyproj
from pyproj import Transformer
transformer = Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True)
df['lon'], df['lat'] = transformer.transform(df['x'].values, df['y'].values)

# Initialize the folium map centered roughly in Oregon
m = folium.Map(location=[45.5, -122.5], zoom_start=7, tiles='OpenStreetMap')

# Add a marker cluster for better display of dense data
marker_cluster = MarkerCluster().add_to(m)

# Function to assign risk based on frequency in the comments
def get_risk_level(comment):
    if pd.isna(comment):
        return "Unknown"
    comment = comment.lower()
    if "5 times or more" in comment or "every yr" in comment:
        return "High"
    elif "every 2 yrs" in comment or "every 5 yrs" in comment:
        return "Medium"
    else:
        return "Low"

# Add risk column
df['Risk'] = df['COMMENTS'].apply(get_risk_level)

# Color mapping
risk_colors = {
    "High": "red",
    "Medium": "orange",
    "Low": "green",
    "Unknown": "gray"
}

# Add markers
for _, row in df.iterrows():
    folium.CircleMarker(
        location=(row['lat'], row['lon']),
        radius=6,
        color=risk_colors.get(row['Risk'], 'blue'),
        fill=True,
        fill_opacity=0.7,
        popup=f"Slide Name: {row['SLIDE_NAME']}<br>Risk: {row['Risk']}<br>Comment: {row['COMMENTS']}"
    ).add_to(marker_cluster)

# Save to HTML
m.save("landslide_map.html")
