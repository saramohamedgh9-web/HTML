from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

greeting = Label(window, text="Hello User", fg='black', bg='white')
button = Button(window, text="Click me", bg='black', fg='white')
entry = Entry(window, fg="yellow", bg="blue", width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(frame, text='Sample Frame')
label.pack()

textbox = Text(frame, fg='green', bg='yellow')
textbox.pack()

window.mainloop()