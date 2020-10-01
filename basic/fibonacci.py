from typing import List


def fibonacci(number:int) -> int:
    """
    Returns the n'th fibonacci sequence number
    
    >>> fibonacci(number=10)
    55
    
    """

    PHI = (1 + 5 ** 0.5) / 2
    return int((PHI**number - (-PHI)**(-number))/(5**0.5))

def fibonacciSequence(number:int) -> List[int]:
    """
    Returns a list of first n fibonacci numbers
    >>> fibonacciSequence(number=10)
    [0,1,1,2,3,5,8,13,21,34,55]
    """
    return [fibonacci(num) for num in range(number + 1)]


if __name__ == "__main__":
    print(fibonacci(number=55))
    print(fibonacciSequence(number=10))
    
