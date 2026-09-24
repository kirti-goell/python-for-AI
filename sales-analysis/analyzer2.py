import pandas as pd
from helpers import calculate_total , format_currency

df = pd.read_csv('data/sales.csv')

totals = []
for index , row in df.iterrows():
    total = calculate_total(row['quantity'] , row['price'])
    totals.append(total)
print(len(df))
print(len(totals))
print(df.columns.tolist())
df['total'] = totals



print('Sales data: ')
for index , row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

grand_sum = df['total'].sum()
formatted_grand_total = format_currency(grand_sum)
print(f"Grand Total : {formatted_grand_total}")