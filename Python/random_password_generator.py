from tkinter import *

import random
window = Tk()
window.title('Tkin+ter password generator Window')

window.geometry('373x100')

def show_password():
    password = random.randint(10000000, 99999999)
    entry.delete(0, END)
    entry.insert(0, password)

greeting = Label(window, text="Hello User", fg='black', bg='white')
greeting.pack()

button = Button(window, text="Click me", bg='black', fg='white', command=show_password)

button.pack()
entry = Entry(window, fg="yellow", bg="blue", width=50)
entry.pack()

window.mainloop()