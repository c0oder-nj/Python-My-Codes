num = int(input("Enter the number: "))
def sum_upto_n(num):
    sum = 0
    if num==0 or num==1:
        return 1
    else:
        sum = sum + num
        num = num-1
        sum_upto_n(num)
