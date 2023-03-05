from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%d %B %Y")
    date_label.config(text=date_string)

    # time_label.after(1000, update)  # updates itself after every 1000ms=1 sec
    window.after(1000, update)


window = Tk()
window.title('clock')

time_label = Label(window, font=("Ariel", 50), fg="#00FF00", bg="black", relief=RAISED, bd=2,padx=10,)
time_label.pack()

day_label = Label(window, font=("Ink Free", 25), relief=RAISED, bd=2,padx=10)
day_label.pack()

date_label = Label(window, font=("Ink Free", 30), relief=RAISED, bd=2,padx=10)
date_label.pack()

update()

window.mainloop()
