import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('FireData23.csv')

fire_counts_per_year = df['FireYear'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(10, 10))
bars = ax.bar(fire_counts_per_year.index, fire_counts_per_year.values)

ax.set_xlabel('Year')
ax.set_ylabel('Fire Count')
ax.set_title('Number of Fires Per Year')

plt.show()
