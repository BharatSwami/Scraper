#!/usr/bin/env python3
# this is great
import socket

mysoct=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysoct.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysoct.send(cmd)

while True:
    data=mysoct.recv(512)
    if len(data)<1:
        break
    print(data.decode())
mysoct.close()