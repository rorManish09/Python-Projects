import requests
import datetime as dt
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
#
# latitude = data["iss_position"]["latitude"]
#
# position = (latitude,longitude)
#TRY THE ABOVE CODE AS WELL

my_lat ="YOUR LATITUDE"
my_lng = "YOUR LONGITUDE"

parameter = {
    "lat":my_lat,
    "lng":my_lng,
    "formatted":0
}
response = requests.get(" https://api.sunrise-sunset.org/json",params=parameter)

response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time = dt.datetime.now()

hours = time.hour
print(sunrise)
print(sunset)
print(hours)