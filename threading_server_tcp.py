""" Multi threadings server for communication based on tcp
    2023/02/18
   ——coding:utf-8——
    """
import socket
import threading
def link_handler(link, client):
    """
        A funcation that link the server and clients, point the func that the threading should execute.
        parameter link: the connection thread work for now 
        parameter client: the client ip&ports, a 2-tuple
        return value = NONE   
    """

    print(" start receving the requests from [%s:%s]... " % (client[0], client[1]))
    while True:
        client_data = link.recv(1024).decode()
        if client_data == "exit":
            print('[%s:%s] have lost the connection with the server!' % (client[0],client[1]))

            break
        print("You just got the messages from [%s:%s],contents: %s" % (client[0],client[1],client_data))
        link.sendall('recv!'.encode())
    link.close()

ip_port =('127.1',9998)
s = socket.socket()
s.bind(ip_port)
s.listen(5)

print('start socket service, waiting for the clients connect...')
while True:
    conn, address = s.accept()
    t = threading.Thread(target=link_handler, args=(conn, address))
    t.start()
