from tkinter import *

t=Tk()
t.geometry('500x500')
f=('Arial',20,'bold')

c=Canvas(t,bg='blue',height=400,width=400)
line=c.create_line(10,10,390,390,fill='white')
# rec=c.create_rectangle(10,20,30,40,fill='white')
# oval=c.create_oval(90.00,20.00,20.00,90.00,fill='white')
# polygon=c.create_polygon(80.00,40.00,60.00,80.00,fill='white')

c.pack()

t.mainloop()