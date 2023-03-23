from typing import Collection, Set
from typing_extensions import TypeAlias


# The set is the Collection of non similar data types 
# a = {1,2,3,4,5,1}
# print(type(a))
# print(a)

# Empty set

# a = {} # This line will create an empty dictionary
# print(type(a))

b = set() # this line will create an empty set
# print(type(b))


# Methods in Set

# Add method adds the element in the set
b.add(5)
b.add(15)
b.add(10)
b.add(20)

print(b)