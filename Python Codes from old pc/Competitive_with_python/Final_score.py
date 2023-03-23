t = int(input())
for i in range(t):
    MyList = []
    Numbers = input();
    for num in Numbers.split():
        if num.isdigit:
            MyList.append(int(num))
    print(max(MyList))
    