import mysql.connector as c
class dbdemo:
    def __init__(self):
        self.con=c.connect(host='localhost',port='8484',user='root',
        password='Pooja@2025',auth_plugin='mysql_native_password')
        print('connection establish successfully..')
    def create_db(self):
        try:
            dbname=input('enter a database name = ')
            query='create database {}'.format(dbname)
            cur=self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print('database created successfully')
        except Exception as e:
            print(e)
    
    def create_table(self):
        try:
            column=[]
            datatype=[]
            # size=input('how many you want add column = ')
            dbname=input('enter a table name = ')
            print('you can insert only a three columns in the table..')
            for i in range(3):
                #  print(i,' column name = ')
                column[i]=input(' column name = ')
                datatype[i]=input(' column\'s datatype is ')
            query='create table {}({},{},{}) values({},{},{})'.format(dbname,column[0],datatype[0],column[1],datatype[1],column[2],datatype[2])
            cur=self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print('table created successfully')
        except Exception as e:
            print(e)

    def insert(self):
        sid=int(input('enter student id = '))
        sname=input('enter student name = ')
        scontact=int(input('enter student contact = '))

        query="insert into bcaty(sid,sname,scontact) values({},'{}',{})".format(sid,sname,scontact)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('record inserted..')

    def delete(self):
        sid=int(input('enter student id you want to delete = '))
        query="delete from bcaty where sid={}".format(sid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('record deleted successfully..')

    def update(self):
        sid=int(input('enter student id where you want to update = '))
        sname=input('enter student new name = ')
        scontact=int(input('enter student new contact = '))

        query="update bcaty set sname='{}',scontact={} where sid={}".format(sname,scontact,sid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('record updated successfully..')

    def all_record(self):
        query='select * from bcaty'
        cur=self.con.cursor()
        cur.execute(query)
        print('fetch data successfully..')
        for row in cur:
            print('sid = ',row[0])
            print('sname = ',row[1])
            print('scontact = ',row[2])


db=dbdemo()

from tkinter import *
t=Tk()
t.geometry('500x500')
f=('Arial',20,'bold')

b=Button(t,text='insert',font=f,command=db.insert)
b.place(x=20,y=10)

b=Button(t,text='update',font=f,command=db.update)
b.place(x=20,y=110)

b=Button(t,text='delete',font=f,command=db.delete)
b.place(x=20,y=210)

b=Button(t,text='all-record',font=f,command=db.all_record)
b.place(x=20,y=310)


t.mainloop()