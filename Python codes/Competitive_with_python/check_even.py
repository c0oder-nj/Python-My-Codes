num = int(input())
check_num = False

if num%2==0:
    check_num = True
else:
    pass

if check_num:
    if 2<=num<=5:
        print("Not Weird")
    elif 6<=num<=20:
        print("Weird")
    elif num>20:
        print("Not Weird")
else:
        print("Weird")

        