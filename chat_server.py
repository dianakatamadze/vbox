import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 9090))
print('Сервер запущен успешно')

users = {}

while True:
    data, addr = s.recvfrom(1024)

    if data == '':
        continue

    user_id = addr[1]
    data = data.decode()
    if data == '__join':
        print(f'Client {user_id} joined chat')
        continue

    if '<nick_check>' in data:
        user_nick = data.split('>=')[1]
        if user_nick not in users.values():
            users.setdefault(addr, user_nick)
            s.sendto('<nick_check_true>'.encode(), addr)
            continue
        else:
            s.sendto('<nick_check_false>'.encode(), addr)
            continue

    data = f'{users.get(addr)}: {data}'
    for user in users:
        if user != addr:
            s.sendto(data.encode(), user)