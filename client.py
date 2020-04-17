#start connection with server 
#make selection 
#call function
from client_algo import diffie_hellman


import socket



def main():
    client_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_s.connect(("127.0.0.1",4567))
    data = client_s.recv(2048).decode("ascii")
    print(data)
    choice = input("Enter Input:")
    if (choice == 'dh'):
        client_s.send(choice.encode())
        diffie_hellman(client_s)

    

if __name__ == "__main__":
    main()