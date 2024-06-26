#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest


class test_review(unittest.TestCase):
    """
    Test the Review class
    """

    def setUp(self):
        """
        Set up for tests
        """
        self.review = Review(text="Great experience!", place_id="1234", user_id="5678")

    def tearDown(self):
        """
        Tear down for tests
        """
        del self.review

    def test_initialization(self):
        """
        Test that the Review instance is correctly initialized
        """
        self.assertEqual(self.review.text, "Great experience!")
        self.assertEqual(self.review.place_id, "1234")
        self.assertEqual(self.review.user_id, "5678")

    def test_text_is_string(self):
        """
        Test that the text attribute is a string
        """
        self.assertIsInstance(self.review.text, str)

    def test_text_not_empty(self):
        """
        Test that the text attribute is not empty
        """
        self.assertTrue(self.review.text)

    def test_place_id_is_string(self):
        """
        Test that the place_id attribute is a string
        """
        self.assertIsInstance(self.review.place_id, str)

    def test_place_id_not_empty(self):
        """Test that the place_id attribute is not empty"""
        self.assertTrue(self.review.place_id)

    def test_user_id_is_string(self):
        """Test that the user_id attribute is a string"""
        self.assertIsInstance(self.review.user_id, str)

    def test_user_id_not_empty(self):
        """Test that the user_id attribute is not empty"""
        self.assertTrue(self.review.user_id)
