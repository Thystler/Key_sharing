import socket,random
import time

def square_and_multiply(x, k, p=None):
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r**2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r

def miller_rabin(p):
    if p == 2:
        return True
    if not (p & 1):
        return False
    r = p - 1
    u = 0
    while r % 2 == 0:
        r >>= 1
        u += 1

    def witness(a):
        z = square_and_multiply(a, r, p)
        if z == 1:
            return False
        for i in range(u):
            z = square_and_multiply(a, 2**i * r, p)
            if z == p -1:
                return False
        return True
    
    for j in range(5):
        a = random.randrange(2, p-2)
        if witness(a):
            return False
    return True

def prime_generation():
    length = 1024
    while True:
        x = random.getrandbits(length)
        if miller_rabin(x):
            break
    return x

def diffie_hellman(client_sock):


    start = time.time()
    prime = prime_generation()
    print(time.time() - start)
    modulo_num = prime
    base_num = random.randrange(prime - 1)
    server_sec = random.randrange(10000)
    client_sock.send("{0},{1}".format(modulo_num,base_num).encode())

    server_pub = (base_num ** server_sec) % modulo_num
    time.sleep(3)
    client_sock.send(str(server_pub).encode())


    client_pub = client_sock.recv(2048).decode("ascii")
    shared_sec = (int(client_pub) ** server_sec) % modulo_num
    return shared_sec
    