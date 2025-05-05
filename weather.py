import requests
import os
from dotenv import load_dotenv


def get_weather(): 
    load_dotenv()
    api_key = os.environ.get('WEATHER_API')
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=-37.7194&lon=144.8916&appid=' + api_key
    resp = requests.get(url)
    data = resp.json()
    weather = data["weather"]
    main = weather[0]['main']
    description =  weather[0]['description']
    icon = weather[0]['icon']
    return(main, description, icon)

