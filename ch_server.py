import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 9090))
print('Сервер запущен ')

users = []

while True:
    data, addr = s.recvfrom(1024)

    if data == '':
        continue

    user_id = addr[1]
    data = data.decode()

    
    if addr not in users:
        users.append(addr)
        print('join')
    
    data = str((addr, data))
    for user in users:
        if user != addr:
            s.sendto(data.encode(), user)