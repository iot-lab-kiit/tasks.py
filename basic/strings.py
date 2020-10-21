from datetime import datetime


def iterative_len(x):
    """Return the len of an iterator without using len
    
        Example:
        >>> a = "hola"
        >>> iterative_len(a)
        >>> 4
    """
    return sum(1 for i in x)


def recursive_len(x):
    """Return the len of a string without using len but recursively
    
        Example:
        >>> a = "hola"
        >>> recursive_len(a)
        >>> 4
    """
    if x == "":
        return 0

    return 1 + recursive_len(x[1:])


def time_difference(time1: str, time2: str, fmt: str = '%H:%M:%S') -> str:
    """
    Returns the difference between `time1` from `time2` as a sting.

    >>> time_difference('12:00:00', '6:00:00')
    '6:00:00'

    >>> time_difference('6:00:00', '12:00:00')
    '6:00:00'
    """

    d1 = datetime.strptime(time1, fmt)
    d2 = datetime.strptime(time2, fmt)

    # Subtracts the largest from the smallest datetime object
    return str(max(d1, d2) - min(d1, d2))

def get_all_substrings_of_String_in_array(x):
    """Get all the possible substrings of a given string in an array
       Note : Existing function required in current file - recursive_len(x)

        Example:
        >>> a="abcd"
        >>> get_all_substrings_of_String_in_array(a)
        ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']
    """
    if x=="":
        return "Empty String"
    n=recursive_len(x);
    arrret=[]
    strapp=""
    for i in range(1,n+1):

        for j in range(n-i+1):

            k=j+i-1

            for l in range(j,k+1):
                strapp=strapp+x[l]
                
            arrret.append(strapp)
            strapp=""
    return arrret

def self_source():
    """
    Prints the source code of this file
    """
    with open(__file__) as f:
        print(f.read(), end='')
