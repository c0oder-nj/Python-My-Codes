class Calculator:
    def __init__(self,num):
        self.number = num
    
    def Square(self):
        print(f"The square of the given number is {self.number**2}")
    
    def SqaureRoot(self):
        print(f"The Square root of the given number is {self.number**0.5}")

    def Cube(self):
        print(f"The cube of the given number is {self.number**3}")

a = Calculator(9)
a.Square()
a.SqaureRoot()
a.Cube()
