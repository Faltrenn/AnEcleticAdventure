import pygame

pygame.init()

class Notas:
    def __init__(self, X, tela):
        self.X = X
        self.Y = 20
        self.tela = tela

    def render(self):
        pygame.draw.circle(self.tela, (0, 0, 0), (self.X, self.Y), 20)
        pygame.draw.circle(self.tela, (0, 0, 255), (self.X, self.Y), 19)

    def tick(self):
        self.Y += 4




