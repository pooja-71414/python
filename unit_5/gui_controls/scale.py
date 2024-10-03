from tkinter import *

t=Tk()
t.geometry('500x500')
f=('Arial',20,'bold')

sc=Scale(t,font=f,orient=HORIZONTAL,from_=1,to=300,length=200,width=40)
sc.place(x=20,y=10)

t.mainloop()