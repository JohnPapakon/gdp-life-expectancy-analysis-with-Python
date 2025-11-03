import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Checking
data=pd.read_csv('all_data.csv')
print(data.head())
print(data.info())
print(data.duplicated().value_counts())
print(data.isnull().sum())

# General statistics for the dataset
print(data.describe())

# Mean and standard deviation of life expectancy per country
print(data.groupby("Country")["Life expectancy at birth (years)"].mean())
print(data.groupby("Country")["Life expectancy at birth (years)"].std())

# Mean GDP per country
print(data.groupby("Country")["GDP"].mean())

# Life expectancy over time (all countries)
sns.lineplot(data=data, x='Year', y='Life expectancy at birth (years)')
plt.title('Life Expectancy over Years (All Countries)')
plt.show()

# GDP over time (all countries)
sns.lineplot(data=data, x='Year', y='GDP')
plt.title('GDP over Years (All Countries)')
plt.show()

# GDP over time by country
sns.lineplot(data=data, x='Year', y='GDP', hue='Country')
plt.title('GDP over Years by Country')
plt.show()

# Iterate through countries and plot a separate scatterplot for each, with individual colors and titles.

plt.figure(figsize=(15, 8))

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']  # adjust length if you have more/less countries
country_names = [
    'Chile', 'China', 'Germany',
    'Mexico', 'United States of America', 'Zimbabwe'
]

for i, country in enumerate(country_names):
    country_data = data[data['Country'] == country]
    plt.subplot(2, 3, i+1)
    plt.scatter(
        x=country_data['Life expectancy at birth (years)'],
        y=country_data['GDP'],
        color=colors[i],
        alpha=0.8
    )
    plt.title(country)
    plt.xlabel('Life expectancy at birth (years)')
    plt.ylabel('GDP in U.S. Dollars')
    # Optional: plt.grid(True)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Country', y='Life expectancy at birth (years)', data=data)
plt.title('Life Expectancy Distribution by Country')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Country', y='GDP', data=data)
plt.title('GDP Distribution by Country')
plt.xticks(rotation=45)
plt.show()

# Overall Pearson correlation
corr_overall = data['GDP'].corr(data['Life expectancy at birth (years)'])
print(f'Overall Pearson correlation: {corr_overall:.3f}')

# Correlation per country with printout
print("Pearson correlation per country:")
for country in data['Country'].unique():
    country_data = data[data['Country'] == country]
    corr = country_data['GDP'].corr(country_data['Life expectancy at birth (years)'])
    print(f'{country}: {corr:.3f}')

# Scatterplot with regression line for overall data
plt.figure(figsize=(8,6))
sns.regplot(x='GDP', y='Life expectancy at birth (years)', data=data, scatter_kws={'alpha':0.6})
plt.title('GDP vs Life Expectancy (Overall)')
plt.xlabel('GDP (U.S. Dollars)')
plt.ylabel('Life Expectancy at Birth (years)')
plt.show()