#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    """Backref to relate the user to the plce to avoid error"""
    """Cascade is to delete all child objects when parent delete"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship(
            "Place", backref="user", cascade="all, delete, delete-orphan"
        )
        reviews = relationship(
            "Review", cascade="all, delete, delete-orphan", backref="user"
        )
