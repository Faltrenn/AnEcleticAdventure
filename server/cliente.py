import socket
import pickle
from server import Player

ip = "localhost"
porta = 50001

obj = Player.Player()

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip, porta))

print(cliente.recv(1024).decode())
cliente.send(pickle.dumps(obj))
