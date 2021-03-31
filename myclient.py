#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    sock.send(input('vvedite ').encode())
    data = sock.recv(1024)
    print(data.decode())
    if data.decode() =='EXIT':
        break
sock.close()

print(data.decode())

