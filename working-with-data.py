# requests lib is used to work with apis
# pandas lib is used to work with data
# matplotlib lib is used to work with visualizations
# pip install requests pandas matplotlib
# datetime deals with date and time
# timedelta represents a diff in time
# think pandas as excel , whatever we can do in excel , we can do with pandas library+ more


import requests
from datetime import datetime , timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os



# get current date and time
today = datetime.now()

# todays date  - 7 days
week_ago = today - timedelta(days = 7)

# converting date into string
# This is because APIs often expect dates in a specific format.
# strftime() converts a date into a string.
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# get paris weather for last week
url = f"https://archive-api.open-meteo.com/v1/archive?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FParis"

response = requests.get(url)
data = response.json()
print(data)







# ----------------------------------------------------------------------------------------------------
# Extract the daily data
daily_data = data['daily']
print(daily_data)

# in excel we have table , but in pandas we have data frame
# create data frame
df = pd.DataFrame({
    'date':daily_data['time'],
    'min_temp':daily_data['temperature_2m_min'],
    'max_temp':daily_data['temperature_2m_max']
})
print(df)

# convert date string to date time
df['date'] = pd.to_datetime(df['date'])
print(df)



# ------------------------------------------------------------------------------------------------------
# this will create the graph, 10 units of width and 6 units height
# marker = 'o' puts circle on every single data point
# df[date]=x axis , df[temp]=y-axis
# label gives the line a name

plt.figure(figsize=(10,6))

plt.plot(
    df['date'],
    df['max_temp'],
    marker='o',
    label='Max Temp'
)

plt.plot(
    df['date'],
    df['min_temp'],
    marker='o',
    label='Min Temp'

)

# Add labels and title
# x axis wale line ko name dega 
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
# title pure graph ko name deta h and displays at top
plt.title('Paris Weather - Past 7 Days')
# plt.legend() displays those names(labels not for title) on the graph.
plt.legend()

# x labels h jo (date) unhe 45 degrees rotate krdo for better redability
plt.xticks(rotation=45)
plt.tight_layout()

# save pic (folder structure m hai , jhn pr .py files dikh rhi h)
plt.savefig('paris_weaher.png')

# this tells the python to show the graph
plt.show()




# -----------------------------------------------------------------------------------------------------
# Save to CSV
# If the data folder doesn't exist, create it. Then save my DataFrame as paris_weather.csv inside that folder, without saving the DataFrame index
if not os.path.exists('data'):
    os.makedirs('data')

# then after creating the folder , vo df ko csv m convert krke save kregi
# agar data csv file vhn already pdi hai to ye use over write krdega agar update kiya hoga df to updated wale se nhi to purana to h hi
# index=False means df me ye initialy -0 1 2 show kr rha tha 1 rowme ab vo ni krega
df.to_csv('data/paris_weather.csv',index=False)
print('Data saved to data/paris_weather.csv')


# API → JSON → Dictionary → DataFrame → Matplotlib → Graph 📈 -> saved data set 
