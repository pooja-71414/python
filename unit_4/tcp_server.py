import socket
server=socket.socket()
host=socket.gethostname()
port=1234

server.bind((host,port))
server.listen(2)

while True:
    c,addr=server.accept()
    print('get connection from : ',addr)
    c.send(bytes('your connection created successfully ',"utf-8"))
    c.close()