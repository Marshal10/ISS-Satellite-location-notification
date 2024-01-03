import requests
from datetime import datetime
import time
import smtplib

MY_LAT = "Your Lattitude as float"
MY_LONG = "Your Longitude as float"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT-5<=iss_latitude<=MY_LAT+5) and (MY_LONG-5<=iss_longitude<=MY_LONG+5):
        return True



def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour=time_now.hour
    if sunset<=hour<=sunrise:
        return True
    
while True:
    time.sleep(60)
    #Send mail only when the sky is dark and if the iss is near your location
    if is_dark() and is_iss_overhead():
        my_email="YOUR EMAIL HERE"
        password="YOUR APP PASSWORD"
        #Gmail: smtp.gmail.com , Hotmail: smtp.live.com, Outlook: outlook.office365.com, Yahoo: smtp.mail.yahoo.com
        smtp_address="SMTP ADDRESS AS ABOVE"

        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(from_addr=my_email,to_addrs="RECEIVER ADDRESS",msg="Subject:Look up.\n\nThe ISS Satellite is above you in the sky.") 