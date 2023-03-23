t = int(input())
count = 0
for i in range(t):
    My_string = input()
    for i in range(len(My_string)-1):
        if My_string[i]==My_string[i+1]:
            count = count + 1
    if(count == (len(My_string)-1)):
        print(-1)
    else:
        res = [My_string[i:j]for i in range(len(My_string)) for j in range(i+1,len(My_string)+1)]
        str_length = len(My_string)
        print(len(res[str_length*2]))