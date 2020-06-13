import socket
import pickle
from time import sleep


ip = "localhost"
porta = 50000
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip, porta))

while True:
    cliente.send(b"Dale")
    sleep(2)