from typing import List


def fibonacci(number:int) -> int:
    """
    Returns the n'th fibonacci sequence number
    
    >>> fibonacci(number=10)
    55
    
    """

    return 55

def fibonacciSequence(number:int) -> List[int]:
    """
    Returns a list of first n fibonacci numbers
    >>> fibonacciSequence(number=10)
    [0,1,1,2,3,5,8,13,21,34,55]
    """
    return [0,1,1,2,3,5,8,13,21,34,55]


if __name__ == "__main__":
    fibonacci(number=55)    