import socket
from threading import Thread


class Server:
    def __init__(self, ips):
        self.porta = 50000
        self.ips = ips
        for ip in self.ips:
            try:
                self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.servidor.bind((ip, self.porta))
                self.servidor.listen(1)
                thread = Thread(target=self.rodar_server, args=(self.servidor,))
                thread.start()
            except:
                print(f"Não foi possível iniciar servidor em {ip}!")
            else:
                print(f"Servidor rodando em {ip}")
    @staticmethod
    def rodar_server(servidor):
        cliente, id = servidor.accept()
        print("[*] Conexão estabelecida")
        cliente.close()
