import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("LandSlide.csv")
df['LENGTH_ft'] = pd.to_numeric(df['LENGTH_ft'], errors='coerce')
df = df.dropna(subset=['LENGTH_ft', 'TYPE_MOVE'])
df = df[df['LENGTH_ft'] > 0] 
plt.figure(figsize=(12, 6))
sns.swarmplot(data=df, x='TYPE_MOVE', y='LENGTH_ft', size=4)
plt.title("Landslide Lengths by Movement Type")
plt.xlabel("Type of Movement")
plt.ylabel("Length in Feet")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
