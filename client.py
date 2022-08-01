import socket
import select
import sys


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct usage!")
    exit()

ipAddress = str(sys.argv[1])
port = int(sys.argv[2])
server.connect((ipAddress, port))

while True:
    sockets_list = [sys.stdin, server]
    read_sockets, write_sockets, error_sockets = select.select(sockets_list, [],[])
    for socks in read_sockets:
        if socks == server:
            mess = socks.recv(2049)
            print(mess)
        else:
            mess = sys.stdin.readline()
            server.send(mess)
            sys.stdout.write("<you>")
            sys.stdout.write(mess)
            sys.stdout.flush()
server.close()  
# server.close()   