import pygame


class Notas:
    def __init__(self):
        self.posY = 16
        self.pos = [332, self.posY]

    def render(self, janela):
        pygame.draw.circle(janela, (0, 0, 0), self.pos, 20)
        pygame.draw.circle(janela, (0, 0, 255), self.pos, 19)

    def tick(self, objTela):
        self.posY += 2
        self.pos = [332, self.posY]
        if (self.posY >= 660 and self.posY <= 680) and True or self.posY >= 720:
            objTela.notas.remove(self)
