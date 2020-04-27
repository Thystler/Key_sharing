from prime_gen import get_prime,get_primitive_root
import socket,random


def diffie_hellman(client_sock):
    #initates a diffiehellman exchange
    n = 512
    prime = get_prime(n)
    print("Prime Generated")
    generator = random.randrange(prime - 1)
    server_sec = random.randrange(prime)

    #sends the modulo and base number with the client 
    client_sock.send("{0},{1}".format(prime,generator).encode())

    server_pub = pow(generator,server_sec,prime)

    #sends the server public key
    client_sock.send(str(server_pub).encode())

    #recv the client public key
    client_pub = int(client_sock.recv(2048).decode("ascii"))
    shared_sec = pow(client_pub,server_sec,prime)
    return shared_sec
    

def elgamal(client_sock):
    prime = get_prime(512)
    print("Prime Generated")
    generator = get_primitive_root(prime)
    server_sec = random.randrange(10000)
    h = pow(generator,server_sec,prime)
    client_sock.send("{0},{1},{2}".format(prime,generator,h).encode())
    data = client_sock.recv(4096).decode("ascii").split(',')
    s = pow(int(data[0]),server_sec,prime)
    m = (int(data[1]) * pow(s,prime-2,prime)) % prime
    return m

