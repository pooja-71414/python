from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def openfile():
    filedialog.askopenfilename()
def savefile():
    filedialog.asksaveasfilename(initialdir='c:\\',
                                 filetypes={
                                     ('textfile(*.txt)','*.txt'),
                                     ('docfile(*.doc)','*.doc')                                     
                                 })

t=Tk()
t.geometry('500x500')
f=('Arial',10,'bold')

my_menu=Menu()
t.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='File',font=f,menu=file_menu)
file_menu.add_cascade(label='New tab',font=f)
file_menu.add_cascade(label='New window',font=f)
file_menu.add_cascade(label='Open',font=f,command=openfile)
file_menu.add_cascade(label='Save',font=f,command=savefile)
file_menu.add_cascade(label='Save as',font=f,command=savefile)
file_menu.add_cascade(label='Save all',font=f)
file_menu.add_cascade(label='Page setup',font=f)
file_menu.add_cascade(label='Print',font=f)
file_menu.add_cascade(label='Close tab',font=f)
file_menu.add_cascade(label='Close window',font=f)
file_menu.add_cascade(label='Exit',font=f)

edit_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='Edit',font=f,menu=edit_menu)
edit_menu.add_cascade(label='Undo',font=f)
edit_menu.add_cascade(label='Cut',font=f)
edit_menu.add_cascade(label='Copy',font=f)
edit_menu.add_cascade(label='Paste',font=f)
edit_menu.add_cascade(label='Delete',font=f)
edit_menu.add_cascade(label='Find',font=f)
edit_menu.add_cascade(label='Find next',font=f)
edit_menu.add_cascade(label='Find previous',font=f)
edit_menu.add_cascade(label='Replace',font=f)
edit_menu.add_cascade(label='GO to',font=f)
edit_menu.add_cascade(label='Select all',font=f)
edit_menu.add_cascade(label='Time/Date',font=f)
edit_menu.add_cascade(label='Font',font=f)

format_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='View',font=f,menu=format_menu)
zoom_menu=Menu(format_menu,tearoff=0)
format_menu.add_cascade(label='Zoom',font=f,menu=zoom_menu)
zoom_menu.add_cascade(label='Zoom in',font=f)
zoom_menu.add_cascade(label='Zoom out',font=f)
format_menu.add_cascade(label='Status bar',font=f)
format_menu.add_cascade(label='Word wrap',font=f)



t.mainloop()