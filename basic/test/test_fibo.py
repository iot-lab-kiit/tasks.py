import unittest
from basic.fibonacci import fibonacci,fibonacciSequence

class FiboText(unittest.TestCase):
    def test_type(self):
        "Testing return type of fibo is int"
        self.assertEqual(type(fibonacci(number=10)),int)

    def test_return(self):
        "Testing fibo(1) == 1"
        self.assertEqual(fibonacci(number=19),55)

    def test_sequence(self):
        "Testing if fibonacciSequence(10) returns [0,1,1,2,3,5,8,13,21,34,55]"
        self.assertListEqual(fibonacciSequence(10),[0,1,1,2,3,5,8,13,21,34,55])


