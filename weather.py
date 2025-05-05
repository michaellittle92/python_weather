import requests
import os
from dotenv import load_dotenv

def get_data(): 
    load_dotenv()
    api_key = os.environ.get('WEATHER_API')
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=-37.7194&lon=144.8916&appid=' + api_key
    resp = requests.get(url)
    data = resp.json()
    return data

def get_weather(data): 
    
    weather = data["weather"]
    main = weather[0]['main']
    description =  weather[0]['description']
    icon = weather[0]['icon']
    return(main, description, icon)

def get_temp(data):
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    print(f"{temp_min}/{temp_max}")

def main(): 
    data = get_data()
    main, description, icon = get_weather(data)
    get_temp(data)

    print(f"main: {main}, description: {description}, icon = {icon}")

main()