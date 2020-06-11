import pygame


class Tela:
    def __init__(self):
        self.no_menu2 = False
        self.largura = 1280
        self.altura = 720
        self.janela = pygame.display.set_mode((self.largura, self.altura), pygame.FULLSCREEN)
        pygame.display.set_caption("He")
        self.rodando = True

    def render(self, imagens):
        self.janela.blit(imagens.menu2_background, imagens.menu2_background.get_rect())

