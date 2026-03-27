from tkinter import *
import random


window=Tk()
window.title("Rock Paper Scissors")
user_score = 0
comp_score=0


title = Label(window,text="Rock Paper Scissors")
title.pack()

user_label = Label(window,text="Your choice:")
user_label.pack()
comp_label = Label(window,text="Computer choice:")
comp_label.pack()


result_label = Label(window,text="",fg="blue")
result_label.pack()

score_label = Label(window,text="Score - You: 0   Computer: 0")
score_label.pack()



def play(choice):
    global user_score, comp_score

    comp=random.choice(["Rock","Paper","Scissors"])

    user_label.config(text="Your choice: "+choice)
    comp_label.config(text="Computer choice: "+comp)

    if choice==comp:
        result="Tie!"
    elif (choice=="Rock" and comp=="Scissors") or (choice=="Paper" and comp=="Rock") or \
         (choice=="Scissors" and comp=="Paper"):
        result="You win!"
        user_score +=1
    else:
        result="Computer wins!"
        comp_score += 1

    result_label.config(text=result)
    score_label.config(text="Score - You: "+str(user_score)+"   Computer: "+str(comp_score))



rock_btn=Button(window,text="Rock",width=10,command=lambda:play("Rock"))
rock_btn.pack()

paper_btn = Button(window,text="Paper",width=10,command=lambda:play("Paper"))
paper_btn.pack()

scissors_btn=Button(window,text="Scissors",width=10,command=lambda:play("Scissors"))
scissors_btn.pack()



def reset():
    global user_score, comp_score
    user_score=0; comp_score=0
    user_label.config(text="Your choice:")
    comp_label.config(text="Computer choice:")
    result_label.config(text="")
    score_label.config(text="Score - You: 0   Computer: 0")


reset_btn = Button(window,text="Reset",width=10,command=reset)
reset_btn.pack()


window.mainloop()