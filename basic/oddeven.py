def isEven(num:int) -> bool:
    """Add the missing code here to make sure that this 
    function returns true only for even numbers
        >>> isEven(num=42)
        True

        >>> isEven(num=3)
        False
    """
    if( num % 2 == 0):
        return True
    else:
        return False
        

def isOdd(num:int) -> bool:
    """Add the missing code here to make sure that this 
    function returns true only for odd numbers

        >>> isOdd(num=3)
        True
    """
    return num%2!=0

if __name__ == "__main__":
    isEven(num=5)
