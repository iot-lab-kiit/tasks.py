from typing import List
from basic.listoperations import addMatrix
import unittest

import green.suite


class TestListOperation(unittest.TestCase):
    def test_type(self):
        "Test type of add matrix"
        self.assertEqual(
            type(
                addMatrix(
                    m1=[
                        [0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8]],
                    m2=[
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]
                )
            ),
            list)

    


doctest_modules = ["basic.listoperations"]



