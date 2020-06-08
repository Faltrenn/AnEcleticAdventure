import pygame

pygame.init()


class Nota:
    def __init__(self, x, tempo):
        self.x = 535 + (x*42)
        self.corda = x
        self.y = 20
        self.tempo = tempo
        self.pos = [self.x, 20]
        self.cor = [(0, 255, 0), (255, 0, 0), (255, 125, 0), (0, 0, 255)]

    def render(self, janela):
        pygame.draw.circle(janela, self.cor[self.corda-1], self.pos, 20)

    def tick(self):
        self.y += 4
        self.pos = [self.x, self.y]
