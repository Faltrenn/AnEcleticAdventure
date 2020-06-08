import pygame


class Player:

    def __init__(self):
        self.btn1 = 1
        self.btn2 = 1
        self.btn3 = 1
        self.btn4 = 1
        self.modo = "normal"
        self.f1 = False
        self.f2 = False
        self.f3 = False
        self.f4 = False
        self.cima = False
        self.baixo = False

    def render(self, janela):
        pygame.draw.circle(janela, (0,255,0), (577,670), 20, self.btn1)
        pygame.draw.circle(janela, (255, 0, 0), (619, 670), 20, self.btn2)
        pygame.draw.circle(janela, (255, 125, 0), (661, 670), 20, self.btn3)
        pygame.draw.circle(janela, (0, 0, 255), (703, 670), 20, self.btn4)

    def tick(self):
        if not (self.cima or self.baixo):
            if self.f1:
                self.btn1 = 8
            if self.f2:
                self.btn2 = 8
            if self.f3:
                self.btn3 = 8
            if self.f4:
                self.btn4 = 8

        if not self.baixo and not self.cima and self.modo == "palhetar" and not (self.cima or self.baixo or (self.f1 or self.f2 or self.f3 or self.f4)):
            self.btn1 = self.btn2 = self.btn3 = self.btn4 = 1


        if self.cima or self.baixo:
            self.btn1 = int(not self.f1)
            self.btn2 = int(not self.f2)
            self.btn3 = int(not self.f3)
            self.btn4 = int(not self.f4)
            print(self.f4)
