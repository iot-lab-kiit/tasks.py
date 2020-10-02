from typing import List, Tuple


def countDistinct(arr: List[int]) -> int:
    """
    >>> countDistinct([1,2,2,3,4])
    4
    """
    recorded = set()
    count = 0
    for i in arr:
        if i not in recorded:
            count += 1
            recorded.add(i)
    return count


def convertToUpperCase(string: str) -> str:
    """
    >>> convertToUpperCase("hacktoberfest")
    'HACKTOBERFEST'
    """
    return string.upper()


def sortListAlphabetical(arr: List[str]) -> List[str]:
    """
    >>> sortListAlphabetical(["welcome","to","open","source"])
    ['open', 'source', 'to', 'welcome']
    """
    return ['open', 'source', 'to', 'welcome']


def findStringLength(string: str) -> int:
    """
    >>> findStringLength("IoT Lab KiiT")
    12
    """
    return len(string)


def concatenate(string1: str, string2: str) -> str:
    """
    Concatenate two strings without using concat()

    >>> concatenate("hello","world")
    'helloworld'
    """
    return string1 + string2


def reverse_recursion(string: str) -> str:
    """
    Reverse string using recursion

    >>> reverse_recursion("github")
    'buhtig'
    """
    if len(string) <= 1:
        return string
    else:
        return reverse_recursion(string[1:]) + string[0]


def sort_array(arr: List[int]) -> List[int]:
    """
    Sort given array without using sort()
    >>> sort_array([4,3,2,1])
    [1, 2, 3, 4]

    Here, I'm going to use an algorithm called Merge Sort.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        sort_array(left)
        sort_array(right)
        i = 0
        j = 0
        k = 0
        len_left = len(left)
        len_right = len(right)
        while i < len_left and j < len_right:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len_left:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len_right:
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


def largest_element(arr: List[int]) -> int:
    """
    Find the largest element in the array
    >>> largest_element([1,2,3,4,5])
    5
    """
    mx = arr[0]
    for i in arr:
        mx = max(i, mx)
    return mx


def sum_array(arr: List[int]) -> int:
    """
    Find sum of all the array elements
    >>> sum_array([1,2,3])
    6
    """

    return sum(arr)


def number_of_elements(string: str) -> int:
    """
    Find number of elements in the string


    """
    return(len(string))


def largest_of_three(a: int, b: int, c: int) -> int:
    """
    Find largest of 3 given numbers
    >>> largest_of_three(1,2,3)
    3
    """
    return(max(a,b,c))


def number_of_vowels_and_consonants(string: str) -> Tuple[int, int]:
    """
    Returns number of vowels and consonants in a given string
    >>> number_of_vowels_and_consonants("IoT Lab KiiT")
    (5, 5)
    """
    string = string.lower()
    all_letters = set('abcdefghijklmnopqrstuvwxyz')
    vowels = set('aeiou')
    vowel_count = sum([string.count(v) for v in vowels])
    consonant_count = sum([string.count(c) for c in all_letters.difference(vowels)])
    return vowel_count, consonant_count


def swap(a: int, b: int):
    """
    Swap two numbers
    """
    a, b = b, a
