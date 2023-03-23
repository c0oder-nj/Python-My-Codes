test_case = int(input())
for _ in range(test_case):
    l = list(map(int,input().split(" ")))
    l.sort()
    mul = max(l)
    flag = 0
    list_1 = []
    for j in range(1,mul+1):
        if mul%j == 0:
            list_1.append((j,mul//j))
    for j in list_1:
        list_2 = []
        list_2.append(j[0]*j[1])
        list_2.append(j[0]//j[1])
        list_2.append(j[0]-j[1])
        list_2.append(j[0]+j[1])
        list_2.sort()
        if l==list_2:
            print(j[0],j[1])
            flag += 1
            break
    if flag==0:
        print(-1,-1)