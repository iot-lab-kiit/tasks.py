from datetime import datetime


def difference(time1: str, time2: str, fmt: str = '%H:%M:%S') -> str:
    """
    Returns the difference between `time1` from `time2` as a `datetime.timedelta` object.

    >>> difference('12:00:00', '6:00:00')
    '6:00:00'

    >>> difference('6:00:00', '12:00:00')
    '6:00:00'
    """

    d1 = datetime.strptime(time1, fmt)
    d2 = datetime.strptime(time2, fmt)

    # Subtracts the largest from the smallest datetime object
    return max(d1, d2) - min(d1, d2)


if __name__ == '__main__':
    print(difference('6:00:00', '12:00:00'))
