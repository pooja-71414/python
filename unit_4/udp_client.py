import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
port=9001
address=(host,port)
msg=input('enter your message : ')
msg=msg.encode('utf-8')
client.sendto(msg,address)

newmsg,address=client.recvfrom(1024)
newmsg=newmsg.decode('utf-8')
print(newmsg)








'''
import socket

# Server configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a message to the server
message = "Hello, Server!"
client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

# Receive a response from the server
data, server = client_socket.recvfrom(4096)
print(f"Received message from server: {data.decode()}")
'''