str = input("Enter your string: ")
count = 0
str = str.lower()
if(" " in str):
    count += 1

if(count==0):
    str_len = len(str) - 1 
    newstr = ""
    while(str_len>=0):
        newstr = newstr + str[str_len];
        str_len -= 1

if(str == newstr):
    print("Your string is palindrome")
elif(str!=newstr):
    print("Your string is not palindrome")

# Nayan