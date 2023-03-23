class Employee:
    Company = "Google"
    salary = 10000
    @property
    def salary_increment(self):
        self.salary = 