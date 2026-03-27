from tkinter import *

root = Tk()

label = Label(root, text="Hello")
label.pack()

def clicked():
    label.config(text="Clicked!")

button = Button(root, text="Click", command=clicked)
button.pack()

root.mainloop()