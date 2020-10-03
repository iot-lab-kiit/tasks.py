from typing import List

def matrixMul(a, b):
    # Initializing Empty Matrix
    c = [[0, 0], [0, 0]]
    # 2x2 matrix multiplication. Essentially O(1)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] = (c[i][j] + (a[i][k] * b[k][j]))

    # Returning the products
    return c

def fibonacci(number:int) -> int:
    # Initializing Magic Matrix
    a = [[1, 1, ], [1, 0]]
    # Initializing Identity Matrix
    res = [[1, 0], [0, 1]]

    # Fast Exponentiation (log(n) complexity)
    while number:
        if number & 1:
            res = matrixMul(res, a)
        number >>= 1
        a = matrixMul(a, a)

    # Return the nth fibonacci number. Could also return res[0][1] instead.
    return res[1][0]


def fibonacciSequence(number:int) -> List[int]:
    """
    Returns a list of first n fibonacci numbers
    >>> fibonacciSequence(number=10)
    [0,1,1,2,3,5,8,13,21,34,55]
    """
    return [fibonacci(num) for num in range(number + 1)]

