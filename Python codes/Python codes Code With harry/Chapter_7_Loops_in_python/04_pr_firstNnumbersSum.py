num = int(input("Enter the number upto you want sum: "))
# i = 1
sum = 0
# while(i<=num):
#     sum = sum + i
#     i = i+1
# print("The sum upto ",num," is: ",sum)

for i in range(1,num+1):
    sum = sum+i
print("The sum upto ",num," is: ",sum)