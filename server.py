import socket
from kex_algo_server import diffie_hellman,elgamal

init_message = """
Welcome to the key exchange server

1: DH - Diffie-hellman
2: el - El-GAMAL

Example input: "DH"
"""

end_msg = """
------------------------------------------------------------------
Key exchange achived with {0}

Key :{1}
------------------------------------------------------------------
"""

def main():
    server_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_s.bind(('127.0.0.1',4567))
    server_s.listen(5)
    while True:
        client_sock,addr = server_s.accept()
        client_sock.send(init_message.encode())
        data = client_sock.recv(2048).decode("ascii")
        
        if (data == 'dh'):
            print ("Request for key exchange: Diffie-Hellman")
            sharedkey = diffie_hellman(client_sock)
            if sharedkey > 0:
                print(end_msg.format(addr,sharedkey))
        elif(data == 'el'):
            print ("Request for key exchange: El-Gamal")
            sharedkey = elgamal(client_sock)
            if sharedkey > 0:
                print(end_msg.format(addr,sharedkey))
            
            

if __name__ == "__main__":
    main()