import random,time,math


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

def get_prime(n):
    length = n
    print(get_primitive_root(101))
    while True:
        x = random.getrandbits(length)
        if miller_rabin(x):
            break
    return x


def get_primitive_root( p ):
		if p == 2:
				return 1
		p1 = 2
		p2 = (p-1) // p1
		while(True):
				g = random.randint( 2, p-1 )
				if(pow( g, (p-1)//p1, p ) != 1):
						if pow( g, (p-1)//p2, p ) != 1:
								return g