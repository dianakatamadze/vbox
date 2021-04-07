import socket

sock = socket.socket()
sock.setblocking(1)
#спрашиваем адрес и порт у клиента (п. 4)
add = input('введите адрес: ') 
port = input('введите порт: ')
#безопасный ввод данных и значения по умолчанию (п. 4)
if add == '':  
    add = 'localhost'
if port == '':
    port = 9090

sock.connect((add, port)) #соединение с сервером

while True:
    data = input('введите: ')
    if data in ('выход','exit'): #выключаем клиента по просьбе (п. 2)
       print('конец связи ')
       break
    sock.send(data.encode()) #Отправка данных серверу

    data = sock.recv(1024) #Прием данных от сервера
    print(data.decode())
