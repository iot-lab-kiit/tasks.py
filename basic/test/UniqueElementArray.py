from collections import Counter 

def countDistinct(arr): 

	# counter method gives dictionary of elements in list 
	# with their corresponding frequency. 
	# using keys() method of dictionary data structure 
	# we can count distinct values in array 
	return len(Counter(arr).keys())	 

if __name__=="__main__": 
	arr = [10, 20, 20, 10, 30, 10] 
	print (countDistinct(arr)) 
