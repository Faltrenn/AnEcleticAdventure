import pygame
from scripts import Tela

relogio = pygame.time.Clock()

tela = Tela.Tela()


while tela.rodando:

    if pygame.display.get_surface() is not None and pygame.get_init():
        tela.render()
        tela.fechar()

    relogio.tick(60)


