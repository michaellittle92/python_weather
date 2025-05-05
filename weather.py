import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('WEATHER_API')
try:
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=-37.7194&lon=144.8916&appid=' + api_key

    resp = requests.get(url)
    data = resp.json()

    print(data)
except Exception as e:
    print(e) 
