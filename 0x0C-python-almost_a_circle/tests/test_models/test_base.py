#!/usr/bin/python3
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantiation(unittest.TestCase):
    """ Unit tests for testing instantiation of the Base class """

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)