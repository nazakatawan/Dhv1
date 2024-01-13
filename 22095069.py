
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import os

# Reading the dataset
world_data_path = 'world-data-2023.csv'
world_data = pd.read_csv(world_data_path)

# Setting the style for the plots
sns.set(style="whitegrid")

# Creating a figure for the dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 15))

# Dashboard Title
fig.suptitle('World Data Analysis 2023 - Nazakat Ali 22095069', fontsize=16)

# Plot 1: Global Population Density Map
# Reading the world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merging the world map with our data
world = world.merge(world_data, how="left", left_on="name", right_on="Country")

# Removing NaN values for proper mapping
world['Density\n(P/Km2)'] = pd.to_numeric(world['Density\n(P/Km2)'].str.replace(",", ""), errors='coerce').fillna(0)

# Plotting the map
world.plot(column='Density\n(P/Km2)', ax=axes[0, 0], legend=True, cmap='OrRd')
axes[0, 0].set_title('Global Population Density')
axes[0, 0].axis('off')

# Plot 2: Agricultural Land Percentage by Country
world_data['Agricultural Land( %)'] = pd.to_numeric(world_data['Agricultural Land( %)'].str.replace("%", ""), errors='coerce')
top_agricultural_countries = world_data.nlargest(10, 'Agricultural Land( %)')
sns.barplot(x='Agricultural Land( %)', y='Country', data=top_agricultural_countries, ax=axes[0, 1], palette="Greens_r")
axes[0, 1].set_title('Top 10 Countries by Agricultural Land Percentage')
axes[0, 1].set_xlabel('Agricultural Land (%)')
axes[0, 1].set_ylabel('Country')

# Plot 3: Birth Rates vs CO2 Emissions
world_data['Co2-Emissions'] = pd.to_numeric(world_data['Co2-Emissions'].str.replace(",", ""), errors='coerce')
sns.scatterplot(x='Birth Rate', y='Co2-Emissions', data=world_data, ax=axes[1, 0], color='purple')
axes[1, 0].set_title('Birth Rates vs CO2 Emissions')
axes[1, 0].set_xlabel('Birth Rate')
axes[1, 0].set_ylabel('CO2 Emissions')

# Plot 4: Unemployment Rate Distribution
world_data['Unemployment rate'] = pd.to_numeric(world_data['Unemployment rate'].str.replace("%", ""), errors='coerce')
sns.histplot(world_data['Unemployment rate'], bins=20, kde=True, ax=axes[1, 1], color='orange')
axes[1, 1].set_title('Unemployment Rate Distribution')
axes[1, 1].set_xlabel('Unemployment Rate (%)')
axes[1, 1].set_ylabel('Frequency')

# Dashboard Description
description = """
This dashboard presents a comprehensive view of various global indicators for 2023:
1. The map highlights the population density across different countries.
2. The agricultural land percentage chart identifies countries with significant agricultural areas.
3. The scatter plot shows the relationship between birth rates and CO2 emissions, offering insights into environmental and demographic factors.
4. The histogram of unemployment rates provides an overview of global economic conditions.
"""
plt.figtext(0.5, 0.05, description, wrap=True, horizontalalignment='center', fontsize=12)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the plot
plt.savefig('world_data_analysis_2023_nazakat_ali_with_description.png')
