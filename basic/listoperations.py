from typing import List


def addMatrix(m1:List[List[int]],m2:List[List[int]]) -> list:
    """
    Returns addition of two matrices
    >>> addMatrix(m1=[[0, 1, 2],[3, 4, 5],[6, 7, 8]],m2=[[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    """
    m=[]
    for i in range(len(m1)):
        r=[]
        for j in range(len(m1[0])):
            r.append(m1[i][j] + m2[i][j])
        m.append(r)            
    return m

def multMatrix(m1:List[List[int]],m2:List[List[int]]) -> list:
    """
    Returns multiplication of two matrices
    """
    return 

def sortLexographic(string:str) -> List[str]:
    """
    Sorts elements in lexographic/dictionary order
    >>> sortLexographic("hello this is example how to sort the word in alphabetical manner")
    ['alphabetical', 'example', 'hello', 'how', 'in', 'is', 'manner', 'sort', 'the', 'this', 'to', 'word']
    """
    str = str.split()
    str = sorted(str)
    return str


def calculateDifferenceBetweenTimePeriod(time1:str,time2:str) -> str:
    """
    Calculates difference between two times given in input and returns
    difference
    >>> calculateDifferenceBetweenTimePeriod("00:00:00","23:59:59")
    '23:59:59'
    """
    #Change below this

    
    return "23:59:59"

def printOwnSourceCode():
    """
    Show the source code of this file
    """

