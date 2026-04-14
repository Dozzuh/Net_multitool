import socket

target_host = "www.google.com"
target_port = 80

# create a socket object
# AF_INET indicates and IPv4 address
# SOCK_STREAM indicates this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecet the client
client.connect((target_host, target_port))

# Connecting to the server and sendind data in bytes

# Send some data
# the b represents send data in bytes
# GET this is the http method to request data
# / this requests the homepage
# HTTP/1.1 the protocol version to use
# Host: google.com this is the http header
# the backslash characters are nessecary at the end as empty line signifies the end.
# GET can be replace with HEAD to only request headers
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

print(response)
client.close()


# Receiving, Printing, and Closinghte connection
