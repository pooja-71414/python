import socket
client=socket.socket()
host=socket.gethostname()
port=3456
client.connect((host,port))

file=open('read_for_ftp.txt','r')
data=file.read()

client.send(bytes(data,'utf-8'))

data1=client.recv(1024).decode('utf-8')
print(data1)

f=open('write_for_ftp.txt','w')
f.write(data1)
