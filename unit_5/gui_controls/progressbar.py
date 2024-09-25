from tkinter import *
from tkinter import ttk
import time

t=Tk()
t.geometry('500x500')
f=('Arial',20,'bold')

def select():
    pb['value']=20
    t.update_idletasks()
    time.sleep(2)
    pb['value']=40
    t.update_idletasks()
    time.sleep(2)
    pb['value']=60
    t.update_idletasks()
    time.sleep(2)
    pb['value']=80
    t.update_idletasks()
    time.sleep(2)
    

pb=ttk.Progressbar(length=200)
# pb=ttk.Progressbar(length=200,mode='indeterminate')
pb.place(x=20,y=70)

b=Button(t,text='Click!',font=f,command=select)
b.place(x=20,y=10)

t.mainloop()