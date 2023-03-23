num = int(input("Enter number for find the factorial: "))
result = 1
# 5! = 1 x 2 x 3 x 4 x 5 

for i in range(1,num+1) :
    result = result * i

print("The factorial of a given number is: "+ str(result)) 