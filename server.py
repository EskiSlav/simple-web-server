from audioop import add
from os import system
import socket

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind(("localhost", 8080))
# become a server socket
serversocket.listen(5)

while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    data = clientsocket.recv(2048)
    clientsocket.send(f"data received: \'{data}\' from address: {address}".encode())
    clientsocket.close()

