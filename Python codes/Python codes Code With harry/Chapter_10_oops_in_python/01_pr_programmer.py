class Programmer:
    def __init__(self,name,age,subunit):
        print("The object is created")
        self.name = name
        self.age = age
        self.subunit = subunit
    
    def getDetails(self):
        print(f"The Name of the programmer is: {self.name}")
        print(f"The age of the programmer is: {self.age}")
        print(f"The subunit of the programmer is: {self.subunit}")

Niraj = Programmer("Niraj",20,"PlayStore")
Niraj.getDetails()
