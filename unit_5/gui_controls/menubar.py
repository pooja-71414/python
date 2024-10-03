from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog


def checkcolor():
    color=colorchooser.askcolor()
    print(color)
    t.config(bg=color[1])
def openfile():
    filedialog.askopenfilename()

t=Tk()
t.geometry('500x500')
f=('Arial',20,'bold')

my_menu=Menu()
t.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='File',font=f,menu=file_menu)
file_menu.add_cascade(label='New',font=f)
file_menu.add_cascade(label='open',font=f,command=openfile)
file_menu.add_cascade(label='save',font=f)

edit_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='Edit',font=f,menu=edit_menu)
edit_menu.add_cascade(label='cut',font=f)
edit_menu.add_cascade(label='copy',font=f)
edit_menu.add_cascade(label='paste',font=f)
edit_menu.add_cascade(label='color',font=f,command=checkcolor)

format_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='Format',font=f,menu=format_menu)
format_menu.add_cascade(label='font',font=f)
format_menu.add_cascade(label='help',font=f)



t.mainloop()