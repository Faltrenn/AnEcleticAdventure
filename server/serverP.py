import socket
import pickle


ip = "localhost"
porta = 50001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip, porta))

server.listen(2)

print(f"Ouvindo em {ip}:{porta}")

while True:
    cliente, id = server.accept()
    print(f"Conectado ao {id}")
    cliente.send(b"Conexao estabelecida")
    obj = pickle.loads(cliente.recv(1024))
    print(obj.msg)
    obj.tick()
    cliente.close()
