#parent class
class Person(object):
    # def __init__ is known as the constructor
    def __init__(self, name, Idbadge):
        self.name = name
        self.Idbadge = Idbadge
    def display(self):
            print("Name:", self.name)
            print("ID Badge:", self.Idbadge)
#child class
class Employee(Person):
    def __init__(self, name, Idbadge, salary):
        super().__init__(name, Idbadge)
        self.salary = salary
    def display(self):
        super().display()
        print("Salary:", self.salary)
    # Create an instance of the Employee class
employee1 = Employee("John Doe", "ID12345", 50000)
# Call the display method to show the employee's information
employee1.display()