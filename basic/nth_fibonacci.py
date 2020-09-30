def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        return -1 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for _ in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b