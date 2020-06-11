import pygame

pygame.init()


class Nota:
    def __init__(self, x, tempo):
        self.x = 535 + (x*42)
        self.corda = x
        self.y = 20
        self.tempo = tempo
        self.pos = [self.x, 20]
        self.cor = [(0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 0, 255)]


    def render(self, janela):
        pygame.draw.circle(janela, self.cor[self.corda-1], self.pos, 20)

    def tick(self, lista, player):
        self.y += 4
        self.pos = [self.x, self.y]


        if(self.y >= 670 and self.y <= 705):
            if((self.corda == 1 and player.btn1 == 0) or (self.corda == 2 and player.btn2 == 0) or (self.corda == 3 and player.btn3 == 0) or (self.corda == 4 and player.btn4 == 0)):
                lista.remove(self)
                player.pontuacao += 1

        if((player.btn1 == 0 or player.btn2 == 0 or player.btn3 == 0 or player.btn4 == 0) and not (self.y >= 670 and self.y <=705)):
            player.pontuacao -= 1

        elif(self.y >= 720):
            player.pontuacao -= 1
            lista.remove(self)

