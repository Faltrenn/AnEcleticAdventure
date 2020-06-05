import pygame


class Notas:
    def __init__(self):
        self.posY = 16
        self.pos = [703, self.posY]


    def render(self, janela):
        pygame.draw.circle(janela, (0, 0, 0), self.pos, 20)
        pygame.draw.circle(janela, (0, 0, 255), self.pos, 19)



    def tick(self, objTela, player):
        self.posY += 2
        self.pos[1] = self.posY

        if ((self.posY >= 660 and self.posY <= 680) and (player.btn4 == 0) and (self.pos[0] == 703)):
            objTela.notas.remove(self)

        if ((self.posY >= 660 and self.posY <= 680) and (player.btn3 == 0) and (self.pos[0] == 661)):
            objTela.notas.remove(self)

        if ((self.posY >= 660 and self.posY <= 680) and (player.btn2 == 0) and (self.pos[0] == 619)):
            objTela.notas.remove(self)

        if ((self.posY >= 660 and self.posY <= 680) and (player.btn1 == 0) and (self.pos[0] == 577)):
            objTela.notas.remove(self)


