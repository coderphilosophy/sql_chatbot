from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)

class PhoneDetail(Base):
    __tablename__ = "phone_details"

    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String(100))
    model_name = Column(String(255))
    os = Column(String(50))
    popularity = Column(Integer)
    best_price = Column(Float, nullable=True)
    sellers_amount = Column(Integer)
    screen_size = Column(Float)
    memory_size = Column(Float)
    battery_size = Column(Float)
    release_date = Column(String(20))
