import requests
from dotenv import load_dotenv
import os

load_dotenv('keys.env')

#Lendo as variaveis de ambiente
API_KEY = os.getenv('API_KEY')
city_name = 'London'
API_URL = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}'

#Carregando as variáveis de ambiente
load_dotenv()

response_api = requests.get(API_URL) 
status_response = response_api.status_code #working = 200
print(status_response)