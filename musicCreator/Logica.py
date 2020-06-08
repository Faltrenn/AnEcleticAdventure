import pygame
from musicCreator import Notas
pygame.init()

class Tela:
    def __init__(self):
        self.janela = pygame.display.set_mode((160, 400))
        self.rodando = True
        self.btn1 = 0
        self.btn2 = 0
        self.btn3 = 0
        self.btn4 = 0
        self.notas = []

    def trigger(self):

        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                pygame.quit()
                pygame.mixer.quit()



                self.rodando = False

            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_a:
                    self.btn1 = 1
                    self.notas.append(Notas.Notas(20, self.janela))
                if eventos.key == pygame.K_s:
                    self.btn2 = 2
                    self.notas.append(Notas.Notas(60, self.janela))
                if eventos.key == pygame.K_j:
                    self.btn3 = 3
                    self.notas.append(Notas.Notas(100, self.janela))
                if eventos.key == pygame.K_k:
                    self.btn4 = 4
                    self.notas.append(Notas.Notas(140, self.janela))

            if eventos.type == pygame.KEYUP:
                if eventos.key == pygame.K_a:
                    self.btn1 = 0
                if eventos.key == pygame.K_s:
                    self.btn2 = 0
                if eventos.key == pygame.K_j:
                    self.btn3 = 0
                if eventos.key == pygame.K_k:
                    self.btn4 = 0

    def render(self):
        self.janela.fill((255, 255, 255))

        # \\ Player
        if self.btn1 == 1:
            pre1 = 0
        else:
            pre1 = 1
        pygame.draw.circle(self.janela, (0, 255, 0), (20, 20), 20, pre1)

        if self.btn2 == 2:
            pre2 = 0
        else:
            pre2 = 1
        pygame.draw.circle(self.janela, (255, 0, 0), (60, 20), 20, pre2)

        if self.btn3 == 3:
            pre3 = 0
        else:
            pre3 = 1
        pygame.draw.circle(self.janela, (255, 125, 0), (100, 20), 20, pre3)

        if self.btn4 == 4:
            pre4 = 0
        else:
            pre4 = 1
        pygame.draw.circle(self.janela, (0, 0, 255), (140, 20), 20, pre4)
        # Player //

        for nota in self.notas:
            nota.render()
            nota.tick()

            if nota.Y > 400:
                self.notas.remove(nota)

        pygame.display.update()

