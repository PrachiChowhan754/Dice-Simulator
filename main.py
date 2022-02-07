import random
from tkinter import *

root = Tk()
root.title("Roll Dice")
root.geometry("500x400")

text_1 = Label(root,text= '',font=("Helvetica",250,'bold'))

def roll_the_dice():
        num_code = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]
        text_1.config(text=f'{random.choice(num_code)}{random.choice(num_code)}')
        text_1.pack()

button_1=Button(root,text="Roll the Dice!",foreground='green',command=roll_the_dice)
button_1.place(x=300,y=0)

root.mainloop()
