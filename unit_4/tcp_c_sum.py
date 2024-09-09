import socket
client=socket.socket()
host=socket.gethostname()
port=5678

client.connect((host,port))
a=client.recv(1024).decode("utf-8")
print(a)

no1=input('enter no1 = ')
client.send(bytes(no1,'utf-8'))
no2=input('enter no2 = ')
client.send(bytes(no2,'utf-8'))
sum=client.recv(1024).decode('utf-8')
print('sum of no1 and no2 is = ',sum)

client.close()