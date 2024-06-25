#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey, FLOAT, Table
from os import getenv
from sqlalchemy.orm import relationship

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        VARCHAR(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        VARCHAR(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    city_id = Column(
        "city_id", VARCHAR(60),
        ForeignKey("cities.id"), nullable=False, unique=True
    )
    user_id = Column(
        "user_id", VARCHAR(60),
        ForeignKey("users.id"), nullable=False, unique=True
    )
    name = Column(
        "name", VARCHAR(128), nullable=False)
    description = Column(
        "description", VARCHAR(1024),
        nullable=False, default="No Description"
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
    latitude = Column("latitude", FLOAT, nullable=True)
    longitude = Column("longitude", FLOAT, nullable=True)
    reviews = relationship(
        "Review", backref="user", cascade="all, delete, delete-orphan"
    )
    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        back_populates="place_amenities",
        viewonly=False,
    )
    if getenv("HBNB_TYPE_STORAGE") != "db":
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity

            amenity_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @property
        def reviews(self):
            from models import storage
            from models.review import Review

            review_list = []
            for review in storage.all(Review).values():
                if review.id in self.amenity_ids:
                    review_list.append(review)
            return review_list

        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity

            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

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
