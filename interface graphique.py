from tkinter import *
import matplotlib.pyplot as plt
from functools import partial

def lunettes():
    root = Tk()
    labl = Label(root, text='Choix de lunettes')
    button1 = Button(root, text='lunettes1', command=partial(affichagelunettes, genre=1))
    button2 = Button(root, text='lunettes2', command=partial(affichagelunettes, genre=2))
    button3 = Button(root, text='lunettes3', command=partial(affichagelunettes, genre=3))
    label.grid(column=0, row=0)
    button1.grid(column=0, row=1)
    button2.grid(column=1, row=1)
    button3.grid(column=0, row=2)
    return


def chapeau():
    return


def moustache():
    return

root = Tk()
label = Label(root, text='interface de commande')
button1 = Button(root, text='lunettes', command=partial(lunettes))
button4 = Button(root, text='chapeau', command=partial(chapeau))
button5 = Button(root, text='moustache', command=partial(moustache))

label.grid(column=0, row=0)
button1.grid(column=0, row=1)
button4.grid(column=1, row=2)
button5.grid(column=0, row=3)

root.mainloop()
