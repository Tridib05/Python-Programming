#Student class – takes name & 3 subject marks, calculates average:
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.marks = [m1, m2, m3]

    def print_average(self):
        avg = sum(self.marks) / 3
        print(f"{self.name}'s Average Marks: {avg:.2f}")
s1 = Student("Ravi", 80, 75, 90)
s1.print_average()


#Account class – with balance & account no, and methods for debit, credit, print:
class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New Balance: {self.balance}")

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def print_balance(self):
        print(f"Account {self.acc_no} Balance: {self.balance}")
a1 = Account("123456789", 5000)
a1.credit(1000)
a1.debit(2000)
a1.print_balance()