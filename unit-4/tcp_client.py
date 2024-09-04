import socket
client=socket.socket()
host=socket.gethostname()
port=1234

client.connect((host,port))
a=client.recv(1024).decode('utf-8')
print(a)
client.close()