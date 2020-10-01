# Program to give the nth fibonacci number in log(n) time.

# Simple 2d matrix multiplication. The function return the product


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

# Essentially applying fast exponentiation on the "Magic Matrix"
# The [1][0] or [0][1] element of the magic matrix raised to the nth power gives the nth fibonacci number


def fibonacci(n):
    # Initializing Magic Matrix
    a = [[1, 1, ], [1, 0]]
    # Initializing Identity Matrix
    res = [[1, 0], [0, 1]]

    # Fast Exponentiation (log(n) complexity)
    while n:
        if n & 1:
            res = matrixMul(res, a)
        n >>= 1
        a = matrixMul(a, a)

    # Return the nth fibonacci number. Could also return res[0][1] instead.
    return res[1][0]


if __name__ == "__main__":
    print(fibonacci(20))
