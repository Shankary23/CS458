import folium
from folium.plugins import HeatMap
import pandas as pd

df = pd.read_csv("FireData23.csv", low_memory=False)
df = df.dropna(subset=['Latitude', 'Longitude'])

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=6)

heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]
HeatMap(heat_data, radius=10).add_to(m)

legend_html = '''
     <div style="position: fixed; 
                 bottom: 50px; left: 50px; width: 150px; height: 180px; 
                 background-color: white; z-index:9999; font-size:14px;
                 box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
                 border-radius: 8px; padding: 10px;">
     <b>Fire Density</b><br>
     <i>Low</i><div style="height: 10px; background: linear-gradient(to right, blue, cyan, lime, yellow, red);"></div><i>High</i>
     </div>
'''

m.get_root().html.add_child(folium.Element(legend_html))

m.save('fire_heatmap.html')
