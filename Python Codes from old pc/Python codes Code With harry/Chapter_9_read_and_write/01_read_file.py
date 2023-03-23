f = open('sample.txt', 'r')
# data = f.read() #This will read the whole file
# data = f.read(5) #This will read the starting five character's of the file
data = f.readline() # this will read the file content line by line
print(data)
f.close()