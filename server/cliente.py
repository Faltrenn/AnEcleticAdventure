import socket
import pickle
from server import Player

ip = "25.123.12.174" # ip local
porta = 25565

obj = Player.Player() # Simula o que seria um objeto real do jogo

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Define o tipo de conexão.
                                                            # 1 parametro: define a conexão com um ipv4
                                                            # 2 parametro: define o tipo de conexão, tcp/ip
cliente.connect((ip, porta)) # Tenta conexão com o servidor

print(cliente.recv(1024).decode())  # Recebe o que o servidor mandou para o cliente e decodifica
                                    # Os dados são enviados e recebidos em bytes
                                    # O parâmetro de "recv()" [e o tamanho máximo do byte que vai ser recebido
cliente.send(pickle.dumps(obj)) # Envia o objeto player codificado em bytes para o servidor
