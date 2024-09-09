import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Connection to hostname on the port
client_socket.connect((host, port))

# Receive no more than 1024 bytes
message = client_socket.recv(1024)

client_socket.close()

print(message.decode('ascii'))
