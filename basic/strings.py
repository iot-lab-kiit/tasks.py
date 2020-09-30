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
