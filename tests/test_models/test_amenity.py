#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_id__is__string(self):
        """"""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is__time(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is__time(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

