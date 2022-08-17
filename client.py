from http import client
import socket


_address = ('localhost', 8080)


client_socket = socket.socket()
client_socket.connect(_address)

client_socket.send("Hello World Message".encode())
data = client_socket.recv(2048).decode()

print(data)
print('Bye')