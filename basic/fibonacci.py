from typing import List

# fibonacci numbers has property that f(n)=f(n-1)+f(n-2)
def fibonacci(number):
    if number<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif number==0: 
        return 0
    # Second Fibonacci number is 1 
    elif number==1: 
        return 1
    else: 
        return fibonacci(number-1)+fibonacci(number-2)   

def fibonacciSequence(number):
    fibonacci_numbers = [0, 1]
    for i in range(2,number+1):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    return fibonacci_numbers


if __name__ == "__main__":
    fibonacci(number=55)    
