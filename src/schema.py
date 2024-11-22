from pydantic import BaseModel

class WeatherSchema(BaseModel):
    date: int
    temperature: float
    min_temperature: float
    max_temperature: float
    main_weather: str
    description_weather: str
    city: str

    class Config:
        from_attributes = True