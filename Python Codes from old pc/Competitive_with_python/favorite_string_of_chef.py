num  = int(input())
for i in range(num):
    n = int(input())
    str1 = input()
    code = str1.find('code')
    chef = str1.find('chef')
    if(chef<code):
        print("WA")
    elif(code<chef):
        print("AC")
    else:
        print("WA")
