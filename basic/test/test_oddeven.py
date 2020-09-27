
import unittest

from basic.oddeven import isEven


class TestOddEven(unittest.TestCase):

    def test_type(self):
        "isEven returns bool"
        self.assertEqual(type(isEven(num=4)),bool)

    def test_expected(self):
        "isEven(2) returns True"
        self.assertEqual(isEven(num=2),True)

doctest_modules = ['basic.oddeven']