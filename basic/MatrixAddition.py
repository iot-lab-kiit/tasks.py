#Add two matrices
A=[]
B=[]
na=int(input("Enter n for n x m matrix A: "))
ma=int(input("Enter m for n x m matrix A: "))

nb=int(input("Enter n for n x m matrix B: "))
mb=int(input("Enter m for n x m matrix B: "))
if(na!=nb or ma!=mb):
    print("Addition not possible")
else:
    print("Enter the elements in A")
    for i in range(na): 
        row=list(map(int,input().split()))
        A.append(row)

    print("Enter the elements in B")
    for i in range(nb): 
        row=list(map(int,input().split()))
        B.append(row)

    print("Matrix A :")
    for i in range(na):
        for j in range(ma):
            print(A[i][j], end=" ")
        print()
       
    print("Matrix B :")
    for i in range(nb):
        for j in range(mb):
            print(B[i][j], end=" ")
        print()

    print("Addition Matrix :")
    for i in range(na):
       for j in range(ma):
          print(A[i][j] + B[i][j], end=" ")
       print()
