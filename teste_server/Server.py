import socket
import pickle
from threading import Thread
from time import sleep


def nova_conexao(conexao):
    while True:
        print(conexao.recv(1024).decode("utf-8"))
        sleep(2)


conectados = 0

ip = "localhost"
porta = 50000
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip, porta))

servidor.listen(2)

while conectados < 2:
    print("tentando conectar")
    conexao, id = servidor.accept()
    print(f"Conectado ao {id}")
    conectados += 1
    thread = Thread(target=nova_conexao, args=(conexao,))
    thread.start()