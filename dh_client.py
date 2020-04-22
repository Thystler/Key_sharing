import socket,time,random



def diffie_hellman(client_s):
    data = client_s.recv(4096).decode("ascii").split(',')
    modulo_num = int(data[0])
    base_num = int(data[1])
    client_sec = random.randrange(10000)
    client_pub = (base_num ** client_sec) % modulo_num
    server_pub = client_s.recv(2048).decode("ascii")
    client_s.send(str(client_pub).encode())
    shared_sec = (int(server_pub) ** client_sec) % modulo_num
    return shared_sec

