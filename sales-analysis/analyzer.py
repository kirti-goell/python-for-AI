# i have created sales - analysis folder just to understan how we have to manage folders , files , paths in real world projects
# data folder is always created for inputs
# output folder is always for outputs


import os

print("Current working directory : ",os.getcwd())

data_path = "../data/paris_weather.csv"
if(os.path.exists(data_path)):
    print(f"Dath path exists : {data_path}")
else:
    print(f"can not find data path : {data_path}")
    print("make sure you were running from sales-analysis module")



