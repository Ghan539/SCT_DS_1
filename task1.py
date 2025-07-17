import pandas as pd
import matplotlib.pyplot as plt

# Load dataset and skip metadata rows
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)

# List of non-country aggregates (World Bank codes for regions/groups)
aggregates = [
    'WLD', 'EAP', 'LCN', 'MEA', 'NAC', 'SAS', 'IBT', 'HIC', 'LIC', 'LMC',
    'UMC', 'ARB', 'CEB', 'EAS', 'EUU', 'FCS', 'HPC', 'IDA', 'IDB',
    'IDX', 'LTE', 'MIC', 'OED', 'SSF'
]

# Filter: Only rows with 3-letter codes (real countries) and not in aggregates
df = df[(df['Country Code'].str.len() == 3) & (~df['Country Code'].isin(aggregates))]

# Get population data for 2022
df_2022 = df[['Country Name', '2022']].dropna()

# Get top 10 most populous countries
top10 = df_2022.sort_values(by='2022', ascending=False).head(10)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(top10['Country Name'], top10['2022'] / 1e6, color='orange')  # Convert to millions
plt.title('Top 10 Most Populous Countries in 2022')
plt.xlabel('Country')
plt.ylabel('Population (in Millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

