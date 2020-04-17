import socket
from server_algo import diffie_hellman

#inital listen for conenction
#decide on protocol to use 
#call the file with said function

init_message = """
Welcome to the key exchange server

1: DH
2: ECDH

Example input: "DH"
"""

def main():
    server_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_s.bind(('127.0.0.1',4567))
    server_s.listen(5)
    while True:
        client_sock,addr = server_s.accept()
        client_sock.send(init_message.encode())
        data = client_sock.recv(2048).decode("ascii")
        print(data)
        print ("Request for key exchange:{0}".format(data))
        diffie_hellman(client_sock)
if __name__ == "__main__":
    main()