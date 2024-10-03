from tkinter import *
t=Tk()
t.geometry('500x500')
t.resizable(False,False)

l=Label(t,text='hello')
l.pack(side=LEFT)
l.grid(row=0,column=1)
l.place()
t.mainloop()