import socket
server=socket.socket()
host=socket.gethostname()
port=1234

server.bind((host,port))
server.listen(2)

while True:
    con,add=server.accept()
    print('get connection from : ',add)
    con.send(bytes('your connection created successfully ','utf-8'))
    con.close()