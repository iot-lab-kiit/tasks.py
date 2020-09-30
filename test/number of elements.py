#Find the largest element of the array

def Find_large(arr):
    """ input array and return the max element of the array
    arr : input array"""
    new_list = list(arr)

    if new_list == 0:
        return None
    max_element = max(new_list)
    return max_element


t_case1 = [1,2,3,4,5,6,7,9,8]
output = Find_large(t_case1)
assert output == 9

t_case2 = [1,-1000,6,7,9,9,9.1]
output = Find_large(t_case2)
assert output == 9.1


print("all test cases passed")
