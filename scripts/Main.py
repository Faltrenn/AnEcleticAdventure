from scripts import Menu, Tela, Imagens
import pygame

pygame.init()

r = pygame.time.Clock()

tela = Tela.Tela()
menu = Menu.Menu(tela)
imagens = Imagens.Imagens()


def render():
    if pygame.display.get_surface() is not None:
        tela.janela.fill((255, 255, 255))
        if menu.no_menu:
            menu.render(imagens)
        elif tela.no_menu2:
            tela.render(imagens)

        pygame.display.update()


def tick():
    if menu.no_menu:
        menu.tick()


while tela.rodando:

    tick()
    render()

    r.tick(60)