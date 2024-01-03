import requests
from datetime import datetime

MY_LAT = "Your Lattitude as float"
MY_LONG = "Your Longitude as float"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

#Extracting the current location of iss satellite
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

if (MY_LAT-5<=iss_latitude<=MY_LAT+5) and (MY_LONG-5<=iss_longitude<=MY_LONG+5):
        print("Look up")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
#Get the sunrise and sunset hour at your location
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
data = response.json()

time_now = datetime.now()
hour=time_now.hour
if sunset<=hour<=sunrise:
        print("It is dark now")