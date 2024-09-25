import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
port=9001
server.bind((host,port))

msg,address=server.recvfrom(1024)
msg=msg.decode('utf-8')
print(msg)

newmsg=msg.upper()
newmsg=newmsg.encode('utf-8')
server.sendto(newmsg,address)







'''
import socket

# Server configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"[*] Server UDP listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    data, address = server_socket.recvfrom(4096)
    print(f"Message {data.decode()} received from {address}")
    server_socket.sendto("I am the server accepting connections...".encode(), address)

    


import socket

# Server configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"[*] Server UDP listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    data, address = server_socket.recvfrom(4096)
    print(f"Message {data.decode()} received from {address}")
    server_socket.sendto("I am the server accepting connections...".encode(), address)
'''