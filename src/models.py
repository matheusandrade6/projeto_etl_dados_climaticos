# Cria as tabelas que vão ser alimentadas no banco de dados

from sqlalchemy import Column, Integer, String, DateTime, Double
from sqlalchemy.sql import func
from database import Base

class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer)
    date = Column(Integer)
    temperature = Column(Double)
    min_temperature = Column(Double)
    max_temperature = Column(Double)
    main_weather = Column(String)
    description_weather = Column(String)
