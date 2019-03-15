# client

import socket

address = ('10.1.12.205', 8001)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

data = s.recv(512)


def sendMessages(command):
    if data.__eq__('ok'):
        s.send(bytes(command, encoding="utf8"))


def CloseSocket():
    s.close()
