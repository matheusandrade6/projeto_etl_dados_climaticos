from controller import weather_data_fetch, add_data_to_weather_table
from dotenv import load_dotenv
import os


load_dotenv('../keys.env')

#Lendo as variaveis de ambiente
API_KEY = os.getenv('API_KEY')
city_name = 'London'

weather_schemas = weather_data_fetch(city_name,API_KEY)

if __name__ == '__main__':
    if weather_schemas:
        add_data_to_weather_table(weather_schemas)
        print(f'Adicionamos {len(weather_schemas)} linhas ao seu banco de dados.')