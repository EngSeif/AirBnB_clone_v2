#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import VARCHAR, Column, ForeignKey, INTEGER, FLOAT, Table
from sqlalchemy.orm import relationship
from os import getenv

class Place(BaseModel, Base):
    """A place to stay"""
    
    __tablename__ = "places"
    city_id = Column(
        "city_id", VARCHAR(60), ForeignKey("cities.id"), nullable=False, unique=True
    )
    user_id = Column(
        "user_id", VARCHAR(60), ForeignKey("users.id"), nullable=False, unique=True
    )
    name = Column(
        "name", VARCHAR(128), nullable=False
    )
    description = Column(
        "description", VARCHAR(1024), nullable=False, default="No Description"
    )
    number_rooms = Column(
        "number_rooms", INTEGER, nullable=False, default=0
    )
    number_bathrooms = Column(
        "number_bathrooms", INTEGER, nullable=False, default=0
    )
    max_guest = Column(
        "max_guest", INTEGER, nullable=False, default=0
    )
    price_by_night = Column(
        "price_by_night", INTEGER, nullable=False, default=0
    )
    latitude = Column(
        "latitude", FLOAT, nullable=True
    )
    longitude = Column(
        "longitude", FLOAT, nullable=True
    )
