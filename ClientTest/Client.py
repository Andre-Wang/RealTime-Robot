# client

import socket

address = ('10.1.12.205', 8001)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

data = s.recv(512)
print('the data received is',data)

# MESSAGE=''
s.send(b'hihi')

s.close()
