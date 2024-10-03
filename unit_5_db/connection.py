import mysql.connector as c
# con=c.connect(host='localhost',port='8484',user='root',password='Pooja@2025',auth_plugin='mysql_native_password')
# print(con)
# con.close()

class dbdemo:
    def __init__(self):
        self.con=c.connect(host='localhost',port='8484',user='root',password='Pooja@2025',database='pooja',auth_plugin='mysql_native_password')
        print('connection establish successfully..')

        queary='create table if not exists bcaty (sid int primary key,sname varchar(100),scontact int(12))'

        cur=self.con.cursor()
        cur.execute(queary)
        print('table created successfully.')

    # insert record..
    def insert_record(self,sid,sname,scontact):
        query="insert into bcaty(sid,sname,scontact) values({},'{}',{})".format(sid,sname,scontact)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('record inserted..')

db=dbdemo()
print('for insert record')
sid=int(input('enter student id = '))
sn=input('enter student name = ')
sc=int(input('enter student contact = '))
db.insert_record(sid,sn,sc)