import requests
from database import SessionLocal, engine, Base
from models import Weather
from schema import WeatherSchema

Base.metadata.create_all(bind=engine)

def weather_data_fetch(city_name: str, API_KEY: str):
    API_URL = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}'
    api_response = requests.get(API_URL)
    if api_response.status_code == 200:
        print(f'Conexão concluída com sucesso. Cod:{api_response.status_code}')
        data = api_response.json()
        return WeatherSchema(date=data['list']['dt'], 
                             temperature=data['list']['main']['temp'],
                             min_temperature=data['list']['main']['temp_min'],
                             max_temperature=data['list']['main']['temp_max'],
                             main_weather=data['list']['weather']['main'],
                             description_weather=data['list']['weather']['description']
                             )
    else:
        return print(f'ResponseCod:{api_response.status_code} {api_response.reason}')
    
def add_data_to_weather_table(weather_schema: WeatherSchema) -> Weather:
    with SessionLocal() as db:
        db_weather = Weather(date=weather_schema.date,
                             temperature=weather_schema.temperature,
                             min_temperature=weather_schema.min_temperature,
                             max_temperature=weather_schema.max_temperature,
                             main_weather=weather_schema.main_weather,
                             description_weather=weather_schema.description_weather
                             )
        db.add(db_weather)
        db.commit()
        db.refresh(db_weather)
    return db_weather