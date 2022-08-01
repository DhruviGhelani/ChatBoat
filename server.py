
import socket
import select
import sys
from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket. SO_REUSEADDR, 1)


print("\n---34---", server, "\t", socket.AF_INET, socket.SOCK_STREAM, "\t")
if len(sys.argv) != 3:
    print("Correct usage") 
    exit()                                                     
ipAddress = str(sys.argv[1])
port = int(sys.argv[2])     
server.bind((ipAddress, port))

server.listen(102)
lists_client = []
def clientChatRoom(conn, addr):
    print("\n" , conn , "\t" , addr)
    conn.send("welcome")
    while True:
        try:
            mess = conn.recv(2049)
            if mess: 
                print("\n <", addr[0], "> ", mess)
                mess_to_send = "<" +addr[0]+"> " + mess
                broadcast(mess_to_send, conn)

            else: 
                remove(conn)
        except:
            continue

def broadcast(mess, connection):
    for client in lists_client:
        if client != connection:
            try: 
                client.send(mess)
            except:
                client.close()
                remove(client)

def remove(connect):
    if connect in lists_client:
        lists_client.remove(connect)

while True:
    conn, addr = server.accept()
    lists_client.append(conn)
    print("\n" + addr[0] + "connected")
    start_new_thread(clientChatRoom, (conn, addr))

conn.close()
server.close()