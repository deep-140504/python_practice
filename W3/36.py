import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from GitHub source (assuming file is downloaded as "ufo-reports.csv")
# df = pd.read_csv("ufo-reports.csv")
df = pd.read_csv("ufo-reports.csv", on_bad_lines='skip')
# Convert date column to datetime format
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')

# Extract year and month
df['Year'] = df['datetime'].dt.year
df['Month'] = df['datetime'].dt.month

# Count sightings per year and find the top 10 years
top_years = df['Year'].value_counts().nlargest(10).index

# Filter data for only the top 10 years
df_top = df[df['Year'].isin(top_years)]

# Create a pivot table (rows: year, columns: month, values: count of sightings)
pivot_ufo = pd.pivot_table(df_top, values='datetime', index='Year', columns='Month', aggfunc='count', fill_value=0)

# Display pivot table
print(pivot_ufo)

# Plot a heatmap for visualization
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_ufo, cmap="YlGnBu", annot=True, fmt="d", linewidths=0.5)
plt.title("Top 10 Years of UFO Sightings vs Each Month")
plt.xlabel("Month")
plt.ylabel("Year")
plt.show()
