import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')

df = pd.read_csv("LandSlide.csv")

type_counts = df['TYPE_MOVE'].value_counts()
threshold = 0.02 * type_counts.sum()
filtered_types = type_counts[type_counts > threshold]
other_count = type_counts[type_counts <= threshold].sum()
filtered_types['Other'] = other_count

#Pie Chart
plt.figure(figsize=(10, 8))
plt.pie(filtered_types, labels=filtered_types.index, radius = 1.2, autopct='%1.1f%%', startangle=140)

plt.show()