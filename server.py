import socket
from dh_server import diffie_hellman

init_message = """
Welcome to the key exchange server

1: DH
2: ECDH

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
        print ("Request for key exchange:{0}".format(data))
        sharedkey = diffie_hellman(client_sock)
        if sharedkey > 0:
            print(end_msg.format(addr,sharedkey))
if __name__ == "__main__":
    main()