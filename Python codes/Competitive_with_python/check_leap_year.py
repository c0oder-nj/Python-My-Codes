year = int(input("Enter the year to check: "))
if year%400 == 0:
    print("leap")
elif year%100==0:
    print("not leap")
elif year%4==0:
    print("leap")
else:
    print("Not leap")
