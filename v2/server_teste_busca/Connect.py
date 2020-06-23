import socket


class Connect:
    def __init__(self):
        self.porta = 50000
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tente_conectar(self, ips):
        for ip in ips:
            print(f"[*] Tentando conexão com {ip}:{self.porta}")
            try:
                self.cliente.connect((ip, self.porta))
            except:
                print(f"[*] Conexão com {ip} falhou!")
            else:
                print(f"[*] Conexão com {ip} foi um sucesso!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.cliente.close()
                self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
