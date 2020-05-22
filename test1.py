from tkinter import *


def print_hello():
    print('hi')


root = Tk()

w = Label(root, text="python test")
b = Button(root, text="heelo python", command=print_hello)
c = Button(root, text="Quit", command=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()