def GCD(a,b):
    if(a==b):
        return a
    elif(a==0):
        return b
    elif(b==0):
        return a
    elif(a>b):
        return GCD(a-b,b)
    else:
        return GCD(a,b-a)

def LCM(a,b):
    return (a*b)/GCD(a,b)

test_case = int(input())
for i in range(test_case):
    a = int(input())
    b = int(input())
    lcm_result = LCM(a,b)
    print(f"{GCD(a,b)} ",end='')
    print('%.0f'%lcm_result)

