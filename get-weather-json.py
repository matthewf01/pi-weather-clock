#Access WUnderground API to retrieve weather data for area

import requests
import urllib
import time

#define my variables
weather_city="Suwanee"
weather_state="GA"
weather_conditions_url = "http://api.wunderground.com/api/c11da38a0c7b7fc3/conditions/q/{}/{}.json".format(weather_state,weather_city)
weather_working_dir = "/home/pi/Documents/pi-weather-clock/weatherconditions.json"

def urlget():
   while (True):
     timenow = time.strftime("%X")
     datenow = time.strftime("%x")
     #UNCOMMENT THIS WHEN READY TO PULL NEW WEATHER DATA; COMMENTED OUT FOR TESTING
    urllib.urlretrieve(weather_conditions_url, weather_working_dir)
    print("{} | {} || Weather Condition JSON retrieved for {}/{}".format(datenow, timenow, weather_state,weather_city))
    time.sleep(600)

while (True):
  urlget()


