import pandas as pd
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv('FireData23.csv')

# Group by general cause
cause_counts = df['GeneralCause'].value_counts()
df = df.dropna(subset=['GeneralCause'])

# Plot
plt.figure(figsize=(12,6))
cause_counts.plot(kind='bar', color='skyblue')
plt.title('Fires and their Causes')
plt.xlabel('Cause of the Fire')
plt.ylabel('Number of Fires')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
