from tkinter import*

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(text="Hello", font=("Arial Bold", 50), fg="orange", bg="olive")
btn = Button(text="Click Me", bg="orange", fg="olive")
entry = Entry(width=10, bg="pink", fg="yellow")
lbl.pack()
btn.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5) 
frame.pack()
label = Label(frame, text="This is a frame", bg="cyan", fg="black")
label.pack()
text=Text(frame, height=5, width=20, bg="cyan", fg="black")
text.pack()


