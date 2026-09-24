# lets get real weather data using free weather api
# requests is a Python library that allows Python to send HTTP requests to websites/APIs.
import requests

latitude = 48.85
longitude = 2.35

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# this sends the get req to the api
response = requests.get(url)

# The API sends the information in JSON format.
# .json() converts that JSON response into a Python dictionary.
data = response.json()

print(data)
type(data)
# dict
data.keys()


# current is the key in data
data["current"]
type(data["current"])
# dict : means dict inisde dict

temperature = data["current"]["temperature_2m"]
# temp is nested inside current
print(f"temperature of Paris is : {temperature}")



# lets move one step ahead

def get_temp(latitude , longitude):
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    response = requests.get(url)
    data = response.json()
    return data['current']['temperature_2m']

paris_temp = get_temp(48.85,2.35)
london_temp = get_temp(51.50,-0.12)
tokyo_temp = get_temp(35.68,139.69)

print(f"temp of paris is : {paris_temp}")
print(f"temp of london is : {london_temp}")
print(f"temp of tokyo is : {tokyo_temp}")