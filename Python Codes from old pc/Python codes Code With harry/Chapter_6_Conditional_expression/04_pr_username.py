user_name = input("Enter your username: ")
lenght = len(user_name)

if(lenght>10):
    print("Your user name is fine ")
elif(lenght<10):
    print("Your username is less than 10 you can't contribute here.")