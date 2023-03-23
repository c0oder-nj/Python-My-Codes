def evil_nj(num):
    i = 1
    l = []
    while(i<=num):
        l.append(i)
        i += 1
    i = len(l) - 1
    while(i>0):
        l.pop(i)
        i -= 1
        val = l.pop(i)
        l.insert(0,val)
    print(l[0])

evil_nj(949306)