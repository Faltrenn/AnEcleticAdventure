import pygame
from scripts import Tela

relogio = pygame.time.Clock()

antes = 0

tela = Tela.Tela()


while tela.rodando:

    if pygame.display.get_surface() is not None and pygame.get_init():
        tela.render(tela.janela, tela)
        tela.fechar()

        if pygame.time.get_ticks() - antes >= 1000:
            tela.notas.append(Tela.Notas.Notas())
            antes = pygame.time.get_ticks()

    relogio.tick(60)


