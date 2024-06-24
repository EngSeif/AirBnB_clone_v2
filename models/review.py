#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """ Review classto store review information """
    """foreignkeys to connect id column in user and places with this table- reviews """
    __tablename__ = 'reviews'
    place_id = Column(String(60),
            ForeignKey('places.id'),
            nullable=False
    user_id = Column(String(60),
        ForeignKey('users.id'),
        nullable=False
    text = Column(String(1024),
        nullable=False)
