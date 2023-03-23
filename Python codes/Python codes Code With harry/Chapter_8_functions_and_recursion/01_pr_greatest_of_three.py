num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def Greatest_of_three(x,y,z):
    if x>y:
        f1 = x
    else:
        f1 = y

    if z>f1:
        return z
    else:
        return f1


print("The greatest number is: ",Greatest_of_three(num1,num2,num3))
