import mysql.connector as c
# con=c.connect(host='localhost',port='8484',user='root',password='Pooja@2025',auth_plugin='mysql_native_password')
# print(con)
# con.close()

class dbdemo:
    def __init__(self):
        self.con=c.connect(host='localhost',port='8484',user='root',
                           password='Pooja@2025',database='pooja',
                           auth_plugin='mysql_native_password')
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

    # fetch all record..
    def fetch_all(self):
        query='select * from bcaty'
        cur=self.con.cursor()
        cur.execute(query)
        print('fetch data successfully..')
        for row in cur:
            print('sid = ',row[0])
            print('sname = ',row[1])
            print('scontact = ',row[2])

    # delete record..
    def delete_record(self,sid):
        query="delete from bcaty where sid={}".format(sid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('record deleted successfully..')

    # update record..
    def update_record(self,sid,sname,scontact):
        query="update bcaty set sname='{}',scontact={} where sid={}".format(sname,scontact,sid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('record updated successfully..')

db=dbdemo()
print('for insert record')
sid=int(input('enter student id = '))
sn=input('enter student name = ')
sc=int(input('enter student contact = '))

db.insert_record(sid,sn,sc)
db.fetch_all()

db.delete_record(3)
db.fetch_all()

db.update_record(6,'hello',47889767)
db.fetch_all()
