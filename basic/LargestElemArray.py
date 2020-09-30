# Largest Element in an array

n = int(input("Size of the array : "))
arr = list(map(int,input().split()))
mx = arr[0]
for i in arr:
    mx = max(i,mx)
print("Largest element of array is : ", mx)    
