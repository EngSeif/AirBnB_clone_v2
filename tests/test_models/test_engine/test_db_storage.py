#!/usr/bin/python3
"""This module to test manage file storage for hbnb clone"""
import unittest
from models.state import State
from models import storage


class TestDBStorage(unittest.TestCase):
    """
    Test DB Storage
    """
    def setUp(self):
        """ Set up the test environment """
        self.db = storage.DBStorage()
        self.db.reload()

    def tearDown(self):
        """ Tear down the test environment """
        self.db.close()

    def test_new(self):
        """ Test adding a new object to the session """
        state = State(name="California")
        self.db.new(state)
        self.assertIn(state, self.db._DBStorage__session())

    def test_save(self):
        """ Test saving changes to the database """
        state = State(name="New York")
        self.db.new(state)
        self.db.save()
        state_key = "{}.{}".format(state.__class__.__name__, state.id)
        self.assertIn(state_key, self.db.all(State))

    def test_delete(self):
        """ Test deleting an object from the session """
        state = State(name="Florida")
        self.db.new(state)
        self.db.save()
        state_key = "{}.{}".format(state.__class__.__name__, state.id)
        self.assertIn(state_key, self.db.all(State))
        self.db.delete(state)
        self.assertNotIn(state_key, self.db.all(State))

    def test_all(self):
        """ Test retrieving all objects from the session """
        state1 = State(name="Texas")
        state2 = State(name="Arizona")
        self.db.new(state1)
        self.db.new(state2)
        self.db.save()
        all_states = self.db.all(State)
        self.assertIn(state1, all_states.values())
        self.assertIn(state2, all_states.values())

    def test_reload(self):
        """ Test reloading the database """
        initial_states = len(self.db.all(State))
        self.assertEqual(initial_states, 0)
        state = State(name="Oregon")
        self.db.new(state)
        self.db.save()
        self.assertEqual(len(self.db.all(State)), 1)
        self.db.reload()
        self.assertEqual(len(self.db.all(State)), initial_states)
