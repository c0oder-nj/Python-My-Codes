class Animal:
    id = "Animals"
    def getInfo(self):
        print(f"Hello I'm class Animal and My id is {self.id}")

class Pets(Animal):
    id = "pets"
    def getInfo(self):
        print(f"Hello I'm class Pets and my id is {self.id}")
        super().getInfo()

class Dog(Pets):
    def bark(self):
        print(f"Hello I'm Dog and I'm barking My name is {self.name}")

obj = Dog()
obj.name = "Tuffi"
obj.bark()
obj.getInfo()