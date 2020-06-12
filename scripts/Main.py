from scripts import Menu, Tela, Imagens, Menu_Escolha, Fontes
import pygame

pygame.init()

r = pygame.time.Clock()

tela = Tela.Tela()
fontes = Fontes.Fontes()
menu_escolha = Menu_Escolha.Menu_Escolha(tela, fontes)
menu = Menu.Menu(tela, fontes)
imagens = Imagens.Imagens()


def render():
    if pygame.display.get_surface() is not None:
        tela.janela.fill((255, 255, 255))
        if menu.no_menu:
            menu.render(imagens)
        elif menu_escolha.menu_escolha:
            menu_escolha.render(imagens)

        pygame.display.update()


def tick():
    if menu.no_menu:
        menu.tick(menu_escolha)
    if menu_escolha.menu_escolha:
        menu_escolha.tick()


while tela.rodando:

    tick()
    render()

    r.tick(60)
