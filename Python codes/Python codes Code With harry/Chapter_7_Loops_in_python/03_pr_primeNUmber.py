num = int(input("Enter the number to check whether it is prime or not: "))
prime = True
for i in range(2,num):
    if num%i==0:
        prime = False
        break

if prime:
    print("The Number is prime")
else:
    print("Given number is not prime")