test_case  = int(input())
for i in range(test_case):
    result = 1
    num = int(input())
    for j in range(1,num+1):
        result = result * j
    print(result)