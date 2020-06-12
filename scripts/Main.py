from scripts import Menu, Tela, Imagens, Menu_Escolha
import pygame

pygame.init()

r = pygame.time.Clock()

tela = Tela.Tela()
menu_escolha = Menu_Escolha.Menu_Escolha(tela)
menu = Menu.Menu(tela)
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


while tela.rodando:

    tick()
    render()

    r.tick(60)
