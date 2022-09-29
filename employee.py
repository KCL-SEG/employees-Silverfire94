"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, hours = 0, commission = 0, contract = 0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.commission = commission
        self.contract = contract

        self.pay = ""



    def get_pay(self):
        return self.monthly_salary() + self.monthly_commission()

    def monthly_salary(self):
        if self.hours:
            self.pay += f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour"
            return self.salary*self.hours
        else:
            self.pay += f"{self.name} works on a monthly salary of {self.salary}"
            return self.salary

    def monthly_commission(self):
        if self.commission:
            if self.contract:
                self.pay += f" and receives a commission for {self.contract} contract(s) at {self.commission}/contract. "
                return self.commission*self.contract
            else:
                self.pay += f" and receives a bonus commission of {self.commission}. "
                return self.commission
        else:
            self.pay += ". "
            return 0

    def __str__(self):
        total_pay = self.get_pay()
        return f"{self.pay} Their total pay is {total_pay}."



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary = 4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', salary = 25, hours = 100)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary = 3000, commission = 200, contract = 4)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', salary = 25, hours = 150, commission = 220, contract = 3)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary = 2000, commission = 1500)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', salary = 30, hours = 120, commission = 600)
