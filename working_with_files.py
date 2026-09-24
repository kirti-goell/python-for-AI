import pandas as pd
import json
import os

# read csv file
df = pd.read_csv('sales-analysis/data/sales.csv')
print('CSV Data : ')
print(df)
# tells the no. of rows and no. of cols
print(f"\nShape: {df.shape[0]} rows , {df.shape[1]} columns")

# calculate total : adding total column
df['total'] = df['quantity'] * df['price']
print("\n With totals: ")
print(df)

# create op directory
# means ek output name se folder bnao and exst_ok = true , agar already exist krta hai to new mt bnana and error b mt dena 
os.makedirs('output', exist_ok=True)

# save as diff formats
#  1. JSON (format good for web APIs)
# orient = records means list of dictionaries and indent = 2 means readable format without this 1 line m sara json
df.to_json('output/sales_data.json', orient = 'records' , indent = 2)

# 2.excel format (good for sharing) , for this we need to do pip install openpyxl
# pandas df k sath normally ek index hota hai , index = false means excel file me index ka extra col ni hoga
df.to_excel('output/sales_data.xlsx' , index = False)

# 3.updated csv
df.to_csv('output/sales_data_with_totals.csv' , index = False)


# printing time
print("\nFiles saved : ")
print("- output/sales_data.json")
print("- output/sales_data.xlxs")
print("- output/sales_data_with_totals.csv")