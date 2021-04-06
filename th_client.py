#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.setblocking(1)

sock.connect(('localhost', 9090)) #соединение с сервером

while True:
    data = input('введите: ')
    if data in ('выход','exit'):
        break
    sock.send(data.encode()) #Отправка данных серверу

    data = sock.recv(1024) #Прием данных от сервера
    print(data.decode())
