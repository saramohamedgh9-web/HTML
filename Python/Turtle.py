import turtle

# create a turtle screen
turtle.Screen().bgcolor("lightblue")

s = turtle.Screen()
s.setup(width=600, height=600)

turtle.title("Turtle Graphics Example")
t = turtle.Turtle()
t.shape("turtle")

# draw a square
for Q in range(4):
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)