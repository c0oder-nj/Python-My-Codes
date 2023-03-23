class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_details(self):
        print(f"Train Name is {self.name} and ticket price is {self.fare}")
        print(f"Availabe seats in this train is {self.seats}")

    def Book_ticket(self):
        num = int(input("Enter the tickets you want to book "))
        if(self.seats>=num):
            print("Your Ticket has been booked successfully")
            self.seats = self.seats - num
        else:
            print(f"Sorry seats are not availabe current status is {self.seats}")
        
    def Cancel_ticket(self):
        num = int(input("Enter the number of tickets you want to cancel "))
        self.seats = self.seats + num
        print("Your ticket has been succesffuly cancelled")

Niraj = Train("Rajdhani Express",120,5)
Niraj.get_details()
Niraj.Book_ticket()
# Niraj.Cancel_ticket()
Niraj.Book_ticket()
Niraj.Book_ticket()
Niraj.get_details()
