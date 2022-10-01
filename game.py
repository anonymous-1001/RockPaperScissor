import tkinter as tk
from PIL import ImageTk,Image
import random

def Scissor():
    option=["Scissor","paper","rock"]
    a=random.choice(option)
    if a=="Scissor":
        score1=0
        score2=0
    elif a=="paper":
        score1=1
    else :
        score2=1
def game():
    tk.Label(screen,text="Computer",font=(("Calibri",20))).grid(row=0,column=5)
    tk.Label(screen, text="Player", font=(("Calibri", 20))).grid(row=0, column=0)
    tk.Label(screen,image=plane_hand).grid(row=1,column=0)
    tk.Label(screen, image=plane_hand).grid(row=1, column=5)
    tk.Label(screen,text=score1,font=("Calibri",20)).grid(row=1)
    tk.Label(screen, text=score2, font=("Calibri", 20)).grid(row=1,column=5)
    rock=tk.Button(screen,text="Rock",font=("Calibri",15)).grid(row=1,column=4)
    paper=tk.Button(screen, text="paper", font=("Calibri", 12)).grid(row=2, column=4)
    scissor=tk.Button(screen, text="scissor", font=("Calibri", 12),command=Scissor).grid(row=3, column=4)

screen=tk.Tk()

score1 = 0
score2 = 0

punch = Image.open("punch_hand.png")
punch = punch.resize((150, 200))
punch = ImageTk.PhotoImage(punch)

sisccors = Image.open("sisccors.png")
sisccors = sisccors.resize((150, 200))
sisccors = ImageTk.PhotoImage(sisccors)

plane_hand = Image.open("plaen_hand.jpg")
plane_hand = plane_hand.resize((150, 200))
plane_hand = ImageTk.PhotoImage(plane_hand)

tk.Button(screen,text="Start",font=("Calibri",15),command=game).grid(row=1,column=4,padx=30)
screen.mainloop()