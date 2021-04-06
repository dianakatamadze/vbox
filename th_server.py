import threading
import socket

print("сервер запущен ")
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0) #Начало прослушивания порта

def cl(conn):
	while True:
		data = conn.recv(1024) #Прием данных от клиента
		conn.send(data) #Отправка данных клиенту

while True:
    conn, addr = sock.accept()
    print("Подключение клиента: ", addr)
    th = threading.Thread(target=cl, args=[conn])
    th.start()