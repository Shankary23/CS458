import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')

df = pd.read_csv("LandSlide.csv")

type_counts = df['TYPE_MOVE'].value_counts()
threshold = 0.02 * type_counts.sum()
filtered_types = type_counts[type_counts > threshold]
other_count = type_counts[type_counts <= threshold].sum()
filtered_types['Other'] = other_count

# Create figure with adjusted size
plt.figure(figsize=(12, 8))

# Pie chart
wedges, _, _ = plt.pie(
    filtered_types,
    labels=None,
    radius=1.2,
    autopct=lambda p: f'{p:.1f}%' if p > 5 else '',  # Only show % > 5
    startangle=140,
    colors=plt.cm.tab20.colors,
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
)

# Create enhanced legend labels with percentages
total = sum(filtered_types)
legend_labels = [
    f"{label} ({value}, {value/total:.1%})" 
    for label, value in zip(filtered_types.index, filtered_types)
]

# Build custom legend
legend = plt.legend(
    wedges,
    legend_labels,
    title="Landslide Types\n(Count, Percentage)",
    loc="upper left",
    bbox_to_anchor=(1.05, 1),
    ncol=1,
    fontsize=9,
    title_fontsize=11,
    framealpha=0.95,
    borderaxespad=0.5,
    handlelength=1.5,
    handletextpad=0.5
)

# Style the legend box
legend.get_frame().set_facecolor('#f5f5f5')
legend.get_frame().set_edgecolor('#333333')
legend.get_frame().set_boxstyle('Round, pad=0.2, rounding_size=0.2')

# Add a title
plt.title('Landslide Type Distribution', pad=20, fontsize=14, fontweight='bold')

# Adjust layout to prevent clipping
plt.tight_layout()
plt.subplots_adjust(right=0.7)  # Make space for legend
plt.show()