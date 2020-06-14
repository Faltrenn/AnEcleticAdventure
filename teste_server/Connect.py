import socket

class Connect:
    def __init__(self, nome_da_sala=None):
        self.nome_da_sala = nome_da_sala
        self.ip = "192.168.1.6"
        self.porta = 50000
        self.ip_atual = 0
        self.ips = []
        for c in range(0, 255):
            self.ips.append("192.168.1." + str(c))
        while self.ip_atual <= 255:
            self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                print(self.ips[self.ip_atual])
                self.cliente.connect((self.ips[self.ip_atual], self.porta))
                self.cliente.send(b"ver")
                self.cliente.recv(1024)
                print(f"Nome da sala: {self.cliente.recv(1024).decode()}")
                self.cliente.close()
            except:
                self.ip_atual += 1
            else:
                print(self.ips[self.ip_atual])
a = Connect()
