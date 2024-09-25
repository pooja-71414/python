from tkinter import *
from tkinter import ttk

t=Tk()
t.geometry('500x500')
f=('Arial',20,'bold')

language=['c++','c language','java','advanced java','php','html','css','js','python']
cb=ttk.Combobox(values=language,font=f)
cb.place(x=20,y=20)

t.mainloop()