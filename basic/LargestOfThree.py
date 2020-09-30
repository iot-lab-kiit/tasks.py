# Find largest of three numbers

a = int(input("First Number -"))
b = int(input("Second Number -"))
c = int(input("Third Number -"))

if a>b and a>c:
  print("Largest no is ", a)
elif b>c and b>a:
  print("Largest no is ", b)
else:
  print("Largest no is ", c)
