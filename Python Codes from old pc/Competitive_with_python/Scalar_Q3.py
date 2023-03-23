def check_divisbility(string):
    str2 = ''
    for ch in string:
        if ch.isalnum():
            str2 += ch
    num = int(str2)
    if(num%30==0):
        return 1
    else:
        return 0
A = input()
print(check_divisbility(A))
