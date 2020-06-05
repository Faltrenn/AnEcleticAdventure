import pygame


class Player:

    def __init__(self):
        self.btn1 = 1
        self.btn2 = 1
        self.btn3 = 1
        self.btn4 = 1

    def render(self, janela):
        pygame.draw.circle(janela, (0,255,0), (577,670), 20, self.btn1)
        pygame.draw.circle(janela, (255, 0, 0), (619, 670), 20, self.btn2)
        pygame.draw.circle(janela, (255, 125, 0), (661, 670), 20, self.btn3)
        pygame.draw.circle(janela, (0, 0, 255), (703, 670), 20, self.btn4)

