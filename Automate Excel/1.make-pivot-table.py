import pandas as pd

# Read Excel File
df = pd.read_excel('xlsx/supermarket_sales.xlsx')

# Select columns: 'Gender', 'Product line', 'Total'
df = df[['Gender', 'Product line', 'Total']]

# Make pivot table
pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)

# Export pivot table to Excel file
pivot_table.to_excel('xlsx/pivot_table.xlsx', 'report', startrow=4)