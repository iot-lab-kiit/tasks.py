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

