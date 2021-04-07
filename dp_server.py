import socket
file=open('log.txt','a') #все служебные сообщения записываем в файл (п. 5)
file.write('сервер запущен ' + '\n')
sock = socket.socket()
try:
    port = input('введите порт: ')
    if port == '':
        port = 9090
    sock.bind(('', port))
    sock.listen(0) #Начало прослушивания порта

        
except OSError: 
    while True: #если порт занят, подбираем свободный (п. 6)
        try:
            port+=1
            sock.bind(('', port))
            sock.listen(0) #Начало прослушивания порта
            break
        except OSError:
            continue
print('Cлушаем порт: ',port) 
file.write('Cлушаем порт: ' + str(port)+ '\n')
while True: #сервер не отключается без клиента (п. 3)
    conn, addr = sock.accept()
    file.write('Подключение клиента: ' + str(addr)+ '\n')
    data = conn.recv(1024) #Прием данных от клиента
    conn.send(data) #Отправка данных клиенту
file.close()