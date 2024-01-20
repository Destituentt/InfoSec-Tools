import socket

target_host = "127.0.0.1"
target_port = 9997

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto(b"WRITE MESSAGE HERE",(target_host, target_port))

# Receive some data
data, address = client.recvfrom(4096)

print(data.decode("utf-8"))
print(address.decode("utf-8"))

client.close()
