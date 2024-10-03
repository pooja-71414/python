from tkinter import *
from tkinter import ttk
import time

t=Tk()
t.geometry('500x500')
# f=('Arial',20,'bold')

sb=Scrollbar(t)
sb.pack(side=RIGHT,fill=y)
lb=Listbox(t,yscrollcommand=sb.set)

for i in range(100):
    lb.insert(i,i)

lb.pack(side=LEFT,fill=BOTH)
sb.config(command=lb.yview)

t.mainloop()