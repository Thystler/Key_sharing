import socket

def diffie_hellman(client_sock):
    #agree on p and g
    #server chooses a and sends client A = g^a mod p
    #recv back B = g^b mod p
    #compute s B^a mod p 
    modulo_num = 23
    base_num = 5
    server_sec = 4
    client_sock.send("{0},{1}".format(modulo_num,base_num).encode())
    server_pub = (base_num ** server_sec) % modulo_num
    client_sock.send(str(server_pub).encode())
    client_pub = client_sock.recv(2048).decode("ascii")
    shared_sec = (int(client_pub) ** server_sec) % modulo_num
    print(shared_sec)