import socket,random

def miller_rabin(x):
    if x % 2 == 0:
        print("hello1")
        return False
    print(9 % 10)
    print(-1 % 10)
    #x-1 = 2**u * r
    r = x - 1
    u = 0
    p = x - 1

    print((x-1)%2)
    assert x-1 == 2**u * r

    while (r)%2 == 0 and r>0:
        r  >>= 1
        u+=1
        #print(r)

    assert x -1 == 2**u *r
    print(r,u)
    witness_req = 5
    for i in range(witness_req):
        a = random.randrange(2,p-2)
        b0 = (a ** r) % x
        if (b0 == p or b0 == 1):
            continue
        
        for n in range(u):
            bn = (b0 ** (2 * n)) % x
            if (bn == p):
                continue
            elif(bn == 1):
                return False
    print(x)
def prime_generation():
    n = 20
    x = int(random.getrandbits(n))

    print(len(str(x)))
    if (miller_rabin(x) == False):
        print("hello")
        return False
    return True

def diffie_hellman(client_sock):
    modulo_num = 23
    base_num = 5
    server_sec = 4
    client_sock.send("{0},{1}".format(modulo_num,base_num).encode())
    server_pub = (base_num ** server_sec) % modulo_num
    client_sock.send(str(server_pub).encode())
    client_pub = client_sock.recv(2048).decode("ascii")
    shared_sec = (int(client_pub) ** server_sec) % modulo_num
    print(shared_sec)
    while (prime_generation() == False):
        pass
    