class Robot:
     def __init__(self, name, model):
        self.name = name
        self.model = model
def display_info(self):
        print("Hi! I am:", self.name)
        print("My model is:", self.model)
robot1 = Robot("Tom", "ModelX")
robot1.display_info()
robot2 = Robot("Jerry", "ModelY")
robot2.display_info()