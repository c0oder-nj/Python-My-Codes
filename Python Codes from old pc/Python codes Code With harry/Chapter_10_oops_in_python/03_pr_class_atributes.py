class example:
    a = 10
    def get_a(self):
        print(f"The value of a is {self.a}")
    @staticmethod
    def greet():
        print("Good coming user")

Niraj = example()
Niraj.a = 0
Niraj.get_a()
Niraj.greet()