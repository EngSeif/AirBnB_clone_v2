#!/usr/bin/python3
""" Test Place"""
from models.place import Place
from unittest.mock import patch, MagicMock
from models import storage
from models.review import Review
from models.amenity import Amenity
from datetime import datetime
import unittest


class test_Place(unittest.TestCase):
    """Test the Place class"""

    def setUp(self):
        """Set up for tests"""
        self.place = Place(city_id="1234", user_id="5678",
                           name="Cozy Apartment",
                           description="A lovely place to stay",
                           number_rooms=2,
                           number_bathrooms=1, max_guest=4, price_by_night=100,
                           latitude=37.7749, longitude=-122.4194)

    def tearDown(self):
        """Tear down for tests"""
        del self.place

    def test_initialization(self):
        """
        Test that the Place instance is correctly initialized
        """
        self.assertEqual(self.place.city_id, "1234")
        self.assertEqual(self.place.user_id, "5678")
        self.assertEqual(self.place.name, "Cozy Apartment")
        self.assertEqual(self.place.description, "A lovely place to stay")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)

    def test_city_id_is_string(self):
        """
        Test that the city_id attribute is a string
        """
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_is_string(self):
        """
        Test that the user_id attribute is a string
        """
        self.assertIsInstance(self.place.user_id, str)

    def test_name_is_string(self):
        """
        Test that the name attribute is a string
        """
        self.assertIsInstance(self.place.name, str)

    def test_description_is_string(self):
        """
        Test that the description attribute is a string
        """
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_is_integer(self):
        """
        Test that the number_rooms attribute is an integer
        """
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_is_integer(self):
        """
        Test that the number_bathrooms attribute is an integer
        """
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_is_integer(self):
        """
        Test that the max_guest attribute is an integer
        """
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_is_integer(self):
        """
        Test that the price_by_night attribute is an integer
        """
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_is_float(self):
        """
        Test that the latitude attribute is a float
        """
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_is_float(self):
        """
        Test that the longitude attribute is a float
        """
        self.assertIsInstance(self.place.longitude, float)

    def test_reviews_relationship_db(self):
        """
        Test the reviews relationship in DB storage
        """
        with patch('models.storage') as mock_storage:
            mock_storage.all.return_value = {
                'review1': Review(place_id=self.place.id),
                'review2': Review(place_id=self.place.id)
            }
            reviews = self.place.reviews
            self.assertIsInstance(reviews, list)
            self.assertEqual(len(reviews), 2)
            for review in reviews:
                self.assertEqual(review.place_id, self.place.id)

    def test_reviews_relationship_filestorage(self):
        """
        Test the reviews relationship in FileStorage
        """
        with patch.object(storage, 'all') as mock_all:
            mock_review = MagicMock()
            mock_review.place_id = self.place.id
            mock_all.return_value.values.return_value = [mock_review]
            reviews = self.place.reviews
            self.assertIsInstance(reviews, list)
            self.assertEqual(len(reviews), 1)
            self.assertEqual(reviews[0].place_id, self.place.id)

    def test_amenities_property(self):
        """
        Test the amenities property
        """
        with patch.object(storage, 'all') as mock_all:
            mock_amenity1 = MagicMock()
            mock_amenity1.id = "1"
            mock_amenity2 = MagicMock()
            mock_amenity2.id = "2"
            mock_all.return_value.values.return_value = [
                mock_amenity1,
                mock_amenity2
            ]
            self.place.amenity_ids = ["1"]
            amenities = self.place.amenities
            self.assertIsInstance(amenities, list)
            self.assertEqual(len(amenities), 1)
            self.assertEqual(amenities[0].id, "1")
