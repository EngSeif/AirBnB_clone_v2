from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="delete", backref="place")
    else:

        @property
        def reviews(self):
            """reviews of places of users"""
            from models import storage
            from models.review import Review

            reviews_of_place = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_of_place.append(value)
            return reviews_of_place
