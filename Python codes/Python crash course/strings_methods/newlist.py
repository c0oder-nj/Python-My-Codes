filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for filename in filenames:
    if(filename.startswith("hpp")):
        x = filename.replace("hpp","h")
        newfilenames.append(x)
    elif(filename.endswith("hpp")):
        x = filename.replace("hpp","h")
        newfilenames.append(x)
    else:
        newfilenames.append(filename)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]