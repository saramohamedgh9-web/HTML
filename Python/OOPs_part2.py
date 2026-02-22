class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add_numbers(self):
        total = self.num1 + self.num2 + self.num3
        print("The sum is:", total)


# Creating objects and using the method
exp1 = Expression(5, 10, 15)
exp1.add_numbers()

exp2 = Expression(2, 4, 6)
exp2.add_numbers()