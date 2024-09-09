import socket
server=socket.socket()
host=socket.gethostname()
port=5678

server.bind((host,port))
server.listen(2)

while True:
    con,addr=server.accept()
    print('get connection from : ',addr)
    con.send(bytes('your connection created successfully ',"utf-8"))

    no1=con.recv(1024).decode('utf-8')
    print('no1 = ',no1)
    no2=con.recv(1024).decode('utf-8')
    print('no2 = ',no2)
    sum=int(no1) + int(no2)
    con.send(bytes(str(sum),'utf-8'))

    con.close()