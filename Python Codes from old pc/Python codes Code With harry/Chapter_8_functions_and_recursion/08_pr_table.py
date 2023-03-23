def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

num = int(input("Enter the number: "))
table(num)