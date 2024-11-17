from pydantic import BaseModel
from sqlalchemy import Double, Integer

class WeatherSchema(BaseModel):
    date: Integer
    temperature: Double
    min_temperature: Double
    max_temperature: Double