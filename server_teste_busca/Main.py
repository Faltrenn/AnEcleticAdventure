from server_teste_busca import Connect, Server
import socket
from threading import Thread


ip = socket.gethostbyname(socket.gethostname())
numero_de_pontos = 0
ip_final = ""
for letra in ip:
    if letra == ".":
        numero_de_pontos += 1
    ip_final += letra
    if numero_de_pontos == 3:
        break
ips = list()
for c in range(0, 256):
    ips.append(ip_final + str(c))

server = Server.Server(ips)

connect = Connect.Connect()

for c in range(0, 256, 2):
    print("inicio")
    thread = Thread(target=connect.tente_conectar, args=(ips[c:c+2],))
    thread.start()
    print("fim")
