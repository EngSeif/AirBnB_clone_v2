#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, VARCHAR
from models.place import place_amenity
from os import getenv
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column("name", VARCHAR(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary=place_amenity, back_populates="amenities"
    )
