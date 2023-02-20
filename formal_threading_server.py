""" Socketserver internally uses IO multiplexing and multi-thread/process mechanism to implement a socket server that processes multiple client requests concurrently. When each client requests connect to the server, the socketserver server will create a "thread" or "process" that is responsible for processing all requests from the current client.
    _coding_:utf-8
    2023/02/19
    _created by:suyiie
    """
import socketserver
    
class Myserver(socketserver.BaseRequestHandler):
        # inheritance class
    def handle(self):
        conn = self.request
        conn.sendall('Hello!'.encode())
        while True:
            data = conn.recv(1024).decode()
            if data == 'exit':
                print('End!')
                break
            print("You got the message:%s from %s" % (data,self.client_address))

            conn.sendall(('Got the message:<%s> ' % data).encode())
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.1' , 9998),Myserver)
    print('socketserver boot!')
    server.serve_forever()

