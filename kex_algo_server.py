from prime_gen import get_prime,get_primitive_root
import socket,random
import time


def diffie_hellman(client_sock):

    #initates a diffiehellman exchange
    start = time.time()
    n = 1024
    prime = get_prime(n)
    print(time.time() - start)
    modulo_num = prime
    generator = random.randrange(prime - 1)
    server_sec = random.randrange(10000)

    #sends the modulo and base number with the client 
    client_sock.send("{0},{1}".format(modulo_num,generator).encode())

    server_pub = (generator ** server_sec) % modulo_num
    time.sleep(3)

    #sends the server public key
    client_sock.send(str(server_pub).encode())

    #recv the client public key
    client_pub = client_sock.recv(2048).decode("ascii")
    shared_sec = (int(client_pub) ** server_sec) % modulo_num
    return shared_sec
    

def elgamal(client_sock):
    prime = get_prime(256)
    generator = get_primitive_root(prime)
    server_sec = random.randrange(10000)
    h = (generator ** server_sec) % prime
    client_sock.send("{0},{1},{2}".format(prime,generator,h).encode())
    data = client_sock.recv(4096).decode("ascii").split(',')
    print(data[0])
    print(data[1])

