from typing import List


def fibonacci(number:int) -> int:
    """
    Returns the n'th fibonacci sequence number
    
    >>> fibonacci(number=10)
    55
    
    """
    a = 0
    b = 1
    if number < 0: 
        print("Incorrect input") 
    elif number == 0: 
        return a 
    elif number == 1: 
        return b 
    else: 
        for _ in range(2,number): 
            c = a + b 
            a = b 
            b = c 
        return b

def fibonacciSequence(number:int) -> List[int]:
    """
    Returns a list of first n fibonacci numbers
    >>> fibonacciSequence(number=10)
    [0,1,1,2,3,5,8,13,21,34,55]
    """
    return [0,1,1,2,3,5,8,13,21,34,55]


if __name__ == "__main__":
    fibonacci(number=55)    