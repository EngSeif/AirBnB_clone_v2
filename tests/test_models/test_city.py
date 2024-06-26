#!/usr/bin/python3
""" Test City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class test_City(unittest.TestCase):
    """ test the city"""

    def setUp(self):
        """
        Set up for tests
        """
        self.city = City(name="San Francisco", state_id="1234")

    def tearDown(self):
        """
        Tear down for tests
        """
        del self.city

    def test_City_init(self):
        """Test that the City instance is correctly initialized"""
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.state_id, "1234")

    def test_name_is_string(self):
        """
        Test that the name attribute is a string
        """
        self.assertIsInstance(self.city.name, str)

    def test_state_id_is_string(self):
        """
        Test that the state_id attribute is a string
        """
        self.assertIsInstance(self.city.state_id, str)

    def test_name_not_empty(self):
        """
        Test that the name attribute is not empty
        """
        self.assertTrue(self.city.name)

    def test_state_id_not_empty(self):
        """
        Test that the state_id attribute is not empty
        """
        self.assertTrue(self.city.state_id)

    def test_relationship(self):
        self.assertTrue(hasattr(self.city, 'places'))
        self.assertEqual(self.city.places, [])
