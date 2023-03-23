import sys

test_case = int(sys.stdin.readline())
for i in range(test_case):
    quantity = int(sys.stdin.readline())
    price = int(sys.stdin.readline())
    if quantity<1000:
        result = price*quantity
        result = float(result)
        print('%.6f'%result)
    elif quantity>1000:
        discount_amount = (price*10)/100
        price = price - discount_amount
        result = price*quantity
        result = float(result)
        print('%.6f'%result)