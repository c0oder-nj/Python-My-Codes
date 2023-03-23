num = int(input("Enter the number: "))
def pattern(n):
    for i in range(n):
        print("*"*(n-i))

pattern(num)