import socket

target_host = "127.0.0.1"
target_port = 9997

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host,target_port))

# Send some data
client.send(b"GET / HTTP/1.1\r\nHost: hacker.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

print(response.decode('utf-8'))
client.close()
