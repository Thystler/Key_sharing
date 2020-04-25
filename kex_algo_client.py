import socket,time,random



def diffie_hellman(client_s):
    #recvieves the modulo and generator
    data = client_s.recv(4096).decode("ascii").split(',')

    #recvs the servers public key
    server_pub = client_s.recv(2048).decode("ascii")

    modulo_num = int(data[0])
    base_num = int(data[1])
    client_sec = random.randrange(10000)
    client_pub = (base_num ** client_sec) % modulo_num

    #sends the client public key
    client_s.send(str(client_pub).encode())
    shared_sec = (int(server_pub) ** client_sec) % modulo_num


    return shared_sec


def elgamal(client_s):
    data = client_s.recv(4096).decode("ascii").split(',')
    prime = int(data[0])
    generator = int(data[1])
    h = int(data[2])
    client_sec = random.randrange(prime)
    s = (h ** client_sec) % prime
    c1 = (generator ** client_sec) % prime
    shared_sec = random.randrange(prime)
    c2 = shared_sec * s
    client_s.send('{0},{1}'.format(c1,c2).encode())
