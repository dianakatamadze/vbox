import socket
import threading
import os


def recv_data(sc):
    while True:
        data = sc.recv(1024).decode()
        print(data)


sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sc.connect(('localhost', 9090))


t1 = threading.Thread(target=recv_data, args=(sc,), daemon=True)
t1.start()

while True:
    data = input('you: ')
    sc.send(data.encode())