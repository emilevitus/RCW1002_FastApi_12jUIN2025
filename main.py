from fastapi import FastAPI 
from datetime import datetime
from dotenv import load_dotenv
import requests
import uvicorn

load_dotenv()
app = FastAPI()

CITY = "Lome"
API_KEY ="e98bd992ad3f4c8b81ac0405d1478348"


def get_weather ():
    weather_ur =f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    try:
        response =  requests.get(weather_ur)
        data = response.json()

        weather = {
            #  'date':data['date'],
            'city':data['name'],
            'temperature':data['main']['temp'],
            'description':data['weather'][0]['description'],

        }

    except Exception as e:
        weather = {
            'city':'unknown',
            'temperature':'N/A',
            'description': 'Unable ti get data'

        }
    return weather
@app.get('/info')
async def get_info():
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%Y-%M-%D")
        formatted_time = current_datetime.strftime("%H:%M:%S")
        weather = get_weather()
        return {
            "date": formatted_date,
            "time": formatted_time,
            "weather" : weather
        }
