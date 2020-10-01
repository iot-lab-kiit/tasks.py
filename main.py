import basic.fibonacci
import basic.listoperations
import basic.mathematics
import basic.oddeven

def main():
    print(
    """
    1. Count distinct elements of an array
    2. Convert string to upper case
    3. Sort a set of strings in ascending alphabetical order
    4. Find length of a string without using len()
    5. Concatenate two strings without using concatenate function
    6. Reverse a string using recursion
    7. Sort an array in ascending order without using sort()
    8. Find the largest element of the array
    9. Find the sum of array elements
    10. Find number of elements in the string
    11. Find largest of 3 elements
    12. Count number of vowels and consonants in a string
    13. Swap two given numbers
    14. Find nPr i.e permutation for given n and r
    15. Find nCr i.e combination for given n and r
    16. Multiply two floating point numbers without using '*' operator
    17. Find quotient and remainder obtained by dividing two numbers
    18. Find average of two given numbers
    19. Find matrix addition of two given matrices
    20. Find matrix multiplication of two given matrices
    21. Sort words in given sentence in lexographic (dictionary) order
    22. Calculate time difference between two given time periods
    23. Print source code of this file.
    24. Find if given number is even
    25. Find if given number is odd
    26. Find n'th fibonacci number for given n
    27. Return fibonacci sequence up to the given number
    """)

//solution of task 1
# cook your dish here
list = [1,2,2,3,4,5,5]
ans = len(set(list))
print(ans)

//solution of task 2
# cook your dish here
s = input()
print(s.upper()) 

//solution of task 3
# cook your dish here
s = input()
sorted_characters = sorted(s)
s = "".join(sorted_characters)
print(s)

//solution of task 4
str = input()
counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)

//solution of task 5
s1 = input()
s2 = input()
print('Concatenated String =', s1 + s2)

//solution of task 6
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input())
print(reverse(a))

//solution of task 7
  
arr = [5, 2, 8, 7, 1];     
temp = 0;    
     
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
     
 
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
     
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    





//solution of task 8
arr = [25, 11, 7, 75, 56];     
max = arr[0];    
for i in range(0, len(arr)):    
   if(arr[i] > max):    
       max = arr[i];           
print("Largest element present in given array: " + str(max));   


//solution of task 9
arr = [25, 11, 7, 75, 56];     
sum = 0   
for i in range(0, len(arr)):
    sum=sum+arr[i]
print(sum); 

//solution of task 10
str = "geeks"
print(len(str)) 

//solution of task 11
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
print("The largest number is",largest)


//solution of task 12
str1 = input()
vowels = 0
consonants = 0
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)


//solution of task 13
num1 = input()
num2 = input()
print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)
temp = num1
num1 = num2
num2 = temp
print("Value of num1 after swapping: ", num1)
print("Value of num2 after swapping: ", num2)

//solution of task 14
import math;  
nval = int(input("Enter value of n: "));  
rval = int(input("Enter value of r: "));  
npr = math.factorial(n)/math.factorial(n-r);  
print("nPr =",npr);  


//solution of task 15
import math;
nval = input("Enter value of n: ");
rval = input("Enter value of r: ");
n = int(nval);
r = int(rval);
npr = math.factorial(n)/math.factorial(n-r);
ncr = npr/math.factorial(r);
print("nCr =",ncr);



//solution of task 16
num1=int(input("Enter a number for num1: "))
num2=int(input("Enter a number for num2: "))
product=0
for i in range (1,num2+1):
    product=product+num1       
print("Multiplication of numbers: ",product) 

//solution of task 17
a=int(input())
b=int(input())
quotient=a//b
remainder=a%b
print("Quotient is:",quotient)
print("Remainder is:",remainder)


//solution of task 18
a=int(input())
b=int(input())
avg = (a+b)/2
print(avg)

//solution of task 19
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)


//solution of task 20
X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  
 
Y = [[10,11,12],  
      [13,14,15],  
      [16,17,18]]  
 
result = [[0,0,0],  
               [0,0,0],  
              [0,0,0]]  
for i in range(len(X)):  
   for j in range(len(Y[0])):  
       for k in range(len(Y)):  
           result[i][j] += X[i][k] * Y[k][j]  
for r in result:  
   print(r)  


//solution of task 21
def sortLexo(my_string): 
  
    words = my_string.split() 
      
    words.sort() 
  
    for i in words: 
        print( i )  

if __name__ == '__main__': 
      
    my_string = "hello this is example how to sort " \ 
              "the word in alphabetical manner"
    # Calling function 
    sortLexo(my_string) 


//solution of task 22
from datetime import datetime
fmt = '%Y-%m-%d %H:%M:%S'
tstamp1 = datetime.strptime('2016-04-06 21:26:27', fmt)
tstamp2 = datetime.strptime('2016-04-07 09:06:02', fmt)
if tstamp1 > tstamp2:
    td = tstamp1 - tstamp2
else:
    td = tstamp2 - tstamp1
td_mins = int(round(td.total_seconds() / 60))
print('The difference is approx. %s minutes' % td_mins)


//solution of task 24
num = int(input())
if(num%2==0):
    print("Even")

//solution of task 25
num = int(input())
if(num%2!=0):
    print("Odd")


//solution of task 26
def fib(n):
	if n <= 1:
		return n

	return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':

	n=int(input())
	print("n'th Fibonacci number is", fib(n))


//solution of task 27
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1