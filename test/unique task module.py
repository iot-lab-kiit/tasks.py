def Count_unique_task(arr):
    """ take input arr and return the no. of unique elements in it

    arr: input array
    return: number of unique elements
    """
    set_list = set(arr)
    #print(set_list)
    return len(set_list)


test= [1,2,3,4,5,5,6,7,1,2,3]
output = Count_unique_task(test)
assert output == 7

test1 = [1,2,3,4,5,6,7]
output = Count_unique_task(test1)
assert output == 7

test2 = []
output = Count_unique_task(test2)
assert output == 0

test3 = [1,1,1,1,1,1,1,1]
output = Count_unique_task(test3)
assert output == 1

print("All test cases passed")

