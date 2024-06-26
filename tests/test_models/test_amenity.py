#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest
from models.place import Place

class TestAmenity(unittest.TestCase):
    """
    Test the Amenity class
    """

    def setUp(self):
        """
        Set up for tests
        """
        self.amenity = Amenity(name="WiFi")

    def tearDown(self):
        """
        Tear down for tests
        """
        del self.amenity

    def test_initialization(self):
        """
        Test that the Amenity instance is correctly initialized
        """
        self.assertEqual(self.amenity.name, "WiFi")

    def test_name_is_string(self):
        """
        Test that the name attribute is a string
        """
        self.assertIsInstance(self.amenity.name, str)

    def test_name_not_empty(self):
        """
        Test that the name attribute is not empty
        """
        self.assertTrue(self.amenity.name)
