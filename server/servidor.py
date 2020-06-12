import socket
import pickle


ip = "25.123.12.174"
porta = 25565

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Define o tipo de conexão.
                                                            # 1 parametro: define a conexão com um ipv4
                                                            # 2 parametro: define o tipo de conexão, tcp/ip

server.bind((ip, porta)) # Define o ip e a porta do server

server.listen(2) # Define o numero máximo de conexões simultâneas

print(f"Ouvindo em {ip}:{porta}")

while True:
    cliente, id = server.accept()   # Aceita a conexão
                                    # cliente: Vai ser a conexão estabelecida, usando esse objeto
                                    # da pra ver as informações recebidas e da pra enviar informações
                                    # id, é um número que é atribuido quando aceita a comunicação, com ele da pra
                                    # diferenciar conexões diferentes
    print(f"Conectado ao {id}")
    cliente.send(b"Conexao estabelecida") # Envia uma string convertida para bytes para o cliente
    obj = pickle.loads(cliente.recv(1024)) # Decodifica a mensagem enviada pelo cliente, o objeto
    print(obj.msg)
    obj.tick()
    cliente.close() # Encerra a conexão
