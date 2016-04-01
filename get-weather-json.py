#Access WUnderground API to retrieve weather data for area

import requests
import urllib

#define my variables
weather_city="Suwanee"
weather_state="GA"
weather_conditions_url = "http://api.wunderground.com/api/c11da38a0c7b7fc3/conditions/q/%s/%s.json" % (weather_state,weather_city)
weather_working_dir = "/home/pi/Documents/pi-weather-clock/weatherconditions.json"

urllib.urlretrieve(weather_conditions_url, weather_working_dir)
