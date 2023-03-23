# This is my python file for viva reading external hai kal python ka

# First come first variable

# variable is a [refer to] memory location where we store data, python is a case sensitive language | Dynamically type language dynmaic language high level easy to understand and good for beginners Gives us various advantage and shorten developement time by providing many libraries and frameworks


# Identifer --> Identifiers are used to identify literals basically name alg alg functions variables classes or jo bhi hai python me apn in chijo ko jis name se identify kr rahe hai 

# Basically in python variable is symbolic name i.e. referencing to any object e.g name = "Jhon" when we check type for name i.e. type(name) this will give as class str that means name is an pointer that referencing an object jhon which is of class str

name = "jhon"
# print(type(name))

a = 50 # variable identifier a is referencing an integer object which holds value 50

a = 50
b = a  
# in this example we have two variable identifier in which they both  referencing to a same integer object which holds value 50 python interpreter does not create another object for b


# in python we have Identifire to identify each and every object uniquely i.e. with the help of id() function
print(type(b),type(a)) # class int

# python don't have data types like float and double to store big numbers [long]

# tokens --> compiler design me compiler jis jis chij ko tokens me badal deta hai vo tokens hai int # ek token ho gaya include ek token ho gaya < token > token iostream token etc


# Data types in python

# 1. Neumeric [integers, complex numbers, float]
# 2. Dictionary [ key value pair]
# 3. Boolean [True or false]
# 4. set [ ]
# 5. Sequence type [ String list tuples]

# list is mutable but tuple is imutable
# intializing an empty list e.g. a = [] // a is an empty list
a = []
# print(type(a)) class list
# List is defined by squre brackets [ ]
# List mutable mtlb ki change kr skte apn uski values ko
# e.g. my_list = [10,20,02,15] 
my_list = [10,20,2,15]
# print(my_list)
my_list[2] = 200
# print(my_list) # We modified the value of list so it is mutable [changable]

# tuples
# tuples are similar to list but they are imutable
# intializing an empty tuple a = () 
a = ()
# print(type(a)) <class 'tuple'>
# tuples are defined by paranthesis ()
my_tuple = (10,"Niraj",2.5,True)

# print(my_tuple[2])
# my_tuple[2] = 10
# print(my_tuple) # error 'tuple' object does not support item assignment

# mtv = tuple

myStr = "This si my string with  double  spaces"
myStr = myStr.replace("  "," ")
print(myStr)

my_list = []
# for i in range(7):
#     name = input("Enter fruit name")
#     my_list.append(name)

# for fruit in my_list:
#     print(fruit,end=" ")

print(my_list)
for i in range(6):
    print(i+1,end=" ")
    marks = int(input("Enter marks of student "))
    my_list.append(marks)

my_list.sort() # stack overflow op bolte me galati kr raha tha vaha uska solutio mil gaya 
# .sort() method kuchh return nahi krti ispliye jab me ise print ke andr or mylist = mylist.sort() krke run kr rhaa the toh ye none de rahi thi jo mistake ho rahi thi 
print(my_list)