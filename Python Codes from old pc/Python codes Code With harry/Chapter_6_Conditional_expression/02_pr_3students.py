marks1 = int(input("Enter marks1: ")) 
marks2 = int(input("Enter marks2: ")) 
marks3 = int(input("Enter marks3: ")) 

sum = marks1+marks2+marks3
if(sum>120):
    print("You are pass")
elif(marks1>33 and marks2>33 and marks3 >33):
    print("You are pass but by grace")