import math
from typing import Tuple


def fact(n):
    """
    Returns the factorial of given n
    >>> factorial(6)
    720
    """
    res = 1

    for i in range(2, n + 1):
        res *= i

def combination(n, r):
    """
    Returns the combination i.e nCr of given
    n and r
    >>> combination(5,3)
    10
    """
    # If either n or r is 0, nCr = 1
    return fact(n) / (fact(r) * fact(n - r))

def permutation(n: int, r: int) -> int:
    """
    Returns the permutation i.e nPr of given 
    n and r
    >>> permutation(5,3)
    60
    """
    # If either n or r is 0, nPr = 1
    if n == 0 or r == 0:
        return 1

    # Initializing varibales
    nFac = 1
    nrFac = 1

    # A single for loop to compute both required values
    for i in range(1, n+1):
        nFac *= i
        if i == (n-r):
            nrFac = nFac

    return nFac//nrFac




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


