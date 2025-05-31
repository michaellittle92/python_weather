from fastapi import FastAPI
from data_manager import get_weather_data


app = FastAPI()

@app.get("/weather_data")
async def weather_data():
    weather_data = get_weather_data()
    return weather_data