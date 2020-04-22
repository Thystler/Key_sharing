from dh_client import diffie_hellman
import socket

end_msg = """
------------------------------------------------------------------
Key exchange achived.

Key :{0}
------------------------------------------------------------------
"""

def main():
    client_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_s.connect(("127.0.0.1",4567))
    data = client_s.recv(2048).decode("ascii")
    print(data)
    choice = input("Enter Input:")
    if (choice == 'dh'):
        client_s.send(choice.encode())
        sharedkey = diffie_hellman(client_s)
        if sharedkey > 0:
            print(end_msg.format(sharedkey))


    

if __name__ == "__main__":
    main()