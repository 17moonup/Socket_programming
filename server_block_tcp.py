""" Server socket programming based on TCP 
    2023/02/17
   --- coding:utf-8 ---
    """

import socket

s = socket.socket()

ip_port = ('127.1',9998)                                    #1. create s object and the ip_port

s.bind(ip_port)                                           #2. bind the socket to the ip_port

s.listen(5)                                               #3. listen up

print('socket service started,waiting for the client connect...')

conn,address = s.accept()

while True:
    client_data = conn.recv(1024).decode()
    if client_data == "exit":
        exit('End!')
    print("message:%s,come from %s" % (client_data,address))
    conn.sendall('Recvd'.encode())

conn.close()
