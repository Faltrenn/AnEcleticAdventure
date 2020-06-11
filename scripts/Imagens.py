import pygame


class Imagens:
    def __init__(self):
        self.caminho = "../imagens/"
        self.menu_background = pygame.image.load(self.caminho + "menu_background.jpg")
        self.menu2_background = pygame.image.load(self.caminho + "menu2_background.jpg")
