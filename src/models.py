# Cria as tabelas que vão ser alimentadas no banco de dados

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from database import Base

class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    temperature = Column(Float)
    min_temperature = Column(Float)
    max_temperature = Column(Float)
    main_weather = Column(String)
    description_weather = Column(String)
    city = Column(String)
