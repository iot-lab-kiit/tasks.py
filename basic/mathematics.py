import math
from typing import Tuple


def factorial(n:int) -> int:
    """
    Returns the factorial of given n
    >>> factorial(6)
    720
    """

    if (n<=1):
        return 1
    return n * factorial(n-1)

def permutation(n:int,r:int) -> int:
    """
    Returns the permutation i.e nPr of given 
    n and r
    >>> permutation(5,3)
    60
    """

    return math.floor(factorial(n) / factorial(n-r))

def combination(n:int,r:int) -> int:
    """
    Returns the combination i.e nCr of given
    n and r
    >>> combination(5,3)
    10
    """
    #Change the code below
    return 10

def multfloat(a:float,b:float) -> float:
    """
    Returns the product of two numbers i.e
    a * b without using the '*' multiplication operator

    >>> multfloat(5,3)
    15.0
    """

    return a / (1 / b)

def quotient_and_remainder(a:int,b:int) -> Tuple[int,int]:
    """
    Returns the quotient and remainder obtained from 
    dividing two given numbers
    
    >>> quotient_and_remainder(5,3)
    (1, 2)

    """

    return (a//b,a%b)

def average(a:int,b:int) -> float:
    """

    Returns average of two given numbers

    >>> average(2,2)
    2.0

    """
    return (a+b)/2


