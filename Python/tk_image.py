from tkinter import *
from PIL import ImageTk, Image  
root = Tk()
root.title('Tkinter Image Sample')      
root.geometry('500x500')
upload = Image.open('pinkbackground.jpg')
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, height=500, width=500)
label.place(x=0, y=0)
label2 = Label(root, text='This is how you add an image to a Tkinter window', fg='lightpink', bg='beige')
label2.place(x=200, y=450)
root.mainloop()