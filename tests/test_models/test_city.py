#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ test the city"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_city_name_is_string_and_not_empty(self):
        """Tests that city name is a string and not empty."""
        """Arrange"""
        city_name = "New York"

        """act"""
        city = City(name=city_name)
        """assert"""
        self.assertIsInstance(city.name, str)
        self.assertNotEmpty(city.name)

