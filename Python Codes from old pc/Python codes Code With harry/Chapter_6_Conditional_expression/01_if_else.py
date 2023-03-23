num = int(input("Enter your Marks out of 100: "))
if(num>90):
    print("you scored A+")
elif(num>75 and num<90):
    print("you scored A")
elif(num>50 and num<75):
    print("you scored B+")
elif(num>30 and num<50):
    print("you scored B")
else:
    print("Sorry you're fail.....")
