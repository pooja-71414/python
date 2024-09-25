import socket
server=socket.socket()
host=socket.gethostname()
port=3456

server.bind((host,port))
server.listen(2)
con,address=server.accept()
print('get connection from : ',address)

data=con.recv(1024).decode('utf-8')
print(data)

a=input('enter a data : ')
con.send(bytes(a,'utf-8'))
