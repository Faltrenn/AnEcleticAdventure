import socket
import pickle
from threading import Thread
from time import sleep


class Server:
    def __init__(self):

        self.conexoes = {}

        self.conectados = 0

        self.ips = []
        for c in range(0, 255):
            self.ips.append("192.168.1." + str(c))
        self.porta = 50000
        self.ip_atual = 0
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while self.ip_atual <= 255:
            print("Tentando")
            try:
                self.servidor.bind((self.ips[self.ip_atual], self.porta))
            except:
                self.ip_atual += 1
            else:
                print(self.ips[self.ip_atual])
                print("Conseguiu")
                break
        self.servidor.listen(2)
        self.conexao = self.id = None
        thread = Thread(target=self.tente_conectar(), args=())
        thread.start()

    def tente_conectar(self):
        while self.conectados < 2:
            print("tentando conectar")
            self.conexao, self.id = self.servidor.accept()
            print(f"Conectado ao {self.id}")
            self.conectados += 1
            thread = Thread(target=self.nova_conexao, args=(self.conexao, "dale",))
            thread.start()

    @staticmethod
    def nova_conexao(conexao, nome="Sem nome"):
        print(f"[*] Sala: {nome}")
        while True:
            data = conexao.recv(1024)
            if data != b"":
                try:
                    msg = pickle.loads(data)
                except:
                    msg = data.decode()
                print(msg)
                conexao.send(b"Recebido")
                if msg == "ver":
                    conexao.send(bytes(nome, "utf-8"))
                    conexao.close()
                    break
                sleep(2)
