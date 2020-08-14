import  pygame
class Notas:
    def __init__(self, corda, tempo):
        self.corda = corda
        self.cores = [(0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 0, 255)]
        self.posy = -15
        self.pos = [519 + (30 * self.corda), self.posy]
        self.tempo = tempo

    def tick(self, delta):
        self.posy += 240 * delta
        self.pos[1] = int(self.posy)

    def render(self, tela):
        pygame.draw.circle(tela.janela, self.cores[self.corda-1], self.pos, 30)


notas_provisorias = []
arquivo = open("../src/musicas/Musica1.txt", "r")
for linha in arquivo:
    for c, caractere in enumerate(linha):
        if c <= 8 and caractere.isdigit() and caractere != "0":
            notas_provisorias.append(Notas(int(caractere), float(linha[9:-1])))

for nota in notas_provisorias:
    print(nota.tempo)