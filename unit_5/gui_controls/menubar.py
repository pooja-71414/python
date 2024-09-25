from tkinter import *
from tkinter import ttk

t=Tk()
t.geometry('500x500')
f=('Arial',20,'bold')

my_menu=Menu()
t.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='File',font=f,menu=file_menu)

file_menu.add_cascade(label='New',font=f)

edit_menu=Menu(my_menu)
my_menu.add_cascade(label='Edit',font=f,menu=edit_menu)

t.mainloop()