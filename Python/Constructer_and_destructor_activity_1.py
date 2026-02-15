class Employee:

    # Initializer constructer
    def __init__(self):
        print("Employee created")
    # Destructor    
    def __del__(self):
        print("Employee destroyed")
emp1 = Employee()
del emp1
        
