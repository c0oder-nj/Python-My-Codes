n=int(input("Enter no. of lines you want to print stars: "))
for i in range(n):
    if (i==0 or i==(n-1)):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")