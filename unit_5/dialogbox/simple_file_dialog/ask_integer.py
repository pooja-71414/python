from tkinter import *
from tkinter.simpledialog import *
t=Tk()
t.geometry('500x500')
f=('Arial',20,'bold')


def hello():
    res=SimpleDialog.askstring('input','what is your fname?')

    if res is not None:
        print(res)
    else:
        print('you don\'t have fname')

b=Button(t,command=hello)
b.place(x=20,y=30)

t.mainloop()