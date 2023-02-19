""" The blocked client socket programming based on TCP
   2023/02/17
  
   """

import socket

s = socket.socket()          #1. creat socket object s
ip_port = ('127.1',9998)                                          #2. create address and port

s.connect_ex(ip_port)                                           #3. connect the IP&port to the Server

s.setblocking(1)                                                #select block mode. 0 means unblock mode

s.settimeout(10)

s.gettimeout()
while True:
    test = input("please input the message and ' exit 'for ending:\n").strip()
    s.sendall(test.encode())
    
    if test == 'exit':
        print('End!')
        break

    data = s.recv(1024).decode()                                       #the func recv() is a block way
    print(data)

s.close()                                                       #4. close the socket
    
