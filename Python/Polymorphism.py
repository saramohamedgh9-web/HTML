class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat. My name is {self.name} and I am {self.age} years old.")
    def make_sound(self):
        print("Meow!")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog. My name is {self.name} and I am {self.age} years old.")
    def make_sound(self):
        print("Woof!")
# Creating objects of Cat and Dog
cat1 = Cat("Commando", 3)
dog1 = Dog("Vincent", 5)

for animal in (cat1, dog1):
    animal.info()
    animal.make_sound()