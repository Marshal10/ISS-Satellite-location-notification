import requests
from datetime import datetime

MY_LAT = "Your Lattitude as float"
MY_LONG = "Your Longitude as float"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data)