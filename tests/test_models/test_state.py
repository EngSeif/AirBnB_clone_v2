#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models import storage
from models.state import State
from models.city import City
from uuid import UUID
from os import getenv


class test_state(unittest.TestCase):
    """ """

    def setUp(self):
        """
        Set Up for tests 
        """
        self.state = State(name="California")
        self.city1 = City(name="San Francisco", state_id=self.state.id)
        self.city2 = City(name="Los Angeles", state_id=self.state.id)

    def tearDown(self):
        """
        Tear Down for tests 
        """
        del self.state
        del self.city1
        del self.city2

    def test_state_init(self):
        self.assertEqual(self.state.name, "California")

    def test_unique_id(self):
        """
        Test If the Id is Unique
        """
        self.assertIsInstance(self.state.id, str)
        self.assertTrue(UUID(self.state.id))
        self.assertIsInstance(self.city1.id, str)
        self.assertTrue(UUID(self.city1.id))
        self.assertIsInstance(self.city2.id, str)
        self.assertTrue(UUID(self.city2.id))

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "Testing DB storage only")
    def test_cities_db_storage(self):
        """
        Test Cities Relationship with DB storage
        """
        storage.new(self.state)
        storage.new(self.city1)
        storage.new(self.city2)
        storage.save()
        self.assertIn(self.city1, self.state.cities)
        self.assertIn(self.city2, self.state.cities)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "Testing file storage only")
    def test_cities_file_storage(self):
        """
        Test Cities Relationship with File storage
        """
        storage.new(self.state)
        storage.new(self.city1)
        storage.new(self.city2)
        storage.save()
        city_list = self.state.cities
        self.assertIn(self.city1, city_list)
        self.assertIn(self.city2, city_list)
