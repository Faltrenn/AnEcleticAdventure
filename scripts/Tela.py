import pygame


class Tela:
    def __init__(self):
        self.no_menu2 = False
        self.largura = 1280
        self.altura = 720
        self.janela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("An Ecletic Adventure")
        self.rodando = True
