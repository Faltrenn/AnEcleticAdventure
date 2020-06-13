from scripts import Menu_Principal, Tela, Imagens, Menu_Escolha, Fontes, Mudar_Menu
import pygame

pygame.init()

r = pygame.time.Clock()

tela = Tela.Tela()
fontes = Fontes.Fontes()
menu_escolha = Menu_Escolha.Menu_Escolha(tela, fontes)
menu_principal = Menu_Principal.Menu_Principal(tela, fontes)

telas = {"menu_principal": menu_principal,
         "menu_escolha": menu_escolha}
mudar_menu = Mudar_Menu.Mudar_Menu(telas)

imagens = Imagens.Imagens()


def render():
    if pygame.display.get_surface() is not None:
        tela.janela.fill((255, 255, 255))
        if menu_principal.aqui:
            menu_principal.render(imagens)
        if menu_escolha.aqui:
            menu_escolha.render(imagens)

        pygame.display.update()


def tick():
    if menu_principal.aqui:
        menu_principal.tick(menu_escolha)
    if menu_escolha.aqui:
        menu_escolha.tick()


while tela.rodando:

    tick()
    render()

    r.tick(60)
