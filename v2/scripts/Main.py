from v2.scripts import Menu_Musicas, Mudar_Menu, Imagens, Tela, Menu_Escolha, Menu_Historia, Menu_Opcoes, Fontes, \
    Menu_Principal
import pygame

pygame.init()

r = pygame.time.Clock()

tela = Tela.Tela()
fontes = Fontes.Fontes()
menu_escolha = Menu_Escolha.Menu_Escolha(tela, fontes)
menu_principal = Menu_Principal.Menu_Principal(tela, fontes)
menu_historia = Menu_Historia.Menu_Historia(tela, fontes)
menu_opcoes = Menu_Opcoes.Menu_Opcoes(tela, fontes)
menu_musicas = Menu_Musicas.Menu_Musicas(tela, fontes)

telas = {"menu_principal": menu_principal,
         "menu_escolha": menu_escolha,
         "menu_historia": menu_historia,
         "menu_opcoes": menu_opcoes,
         "menu_musicas": menu_musicas}

mudar_menu = Mudar_Menu.Mudar_Menu(telas)

imagens = Imagens.Imagens()


def render():
    if pygame.display.get_surface() is not None:
        tela.janela.fill((255, 255, 255))
        if menu_principal.aqui:
            menu_principal.render(imagens)
        if menu_escolha.aqui:
            menu_escolha.render(imagens)
        if menu_historia.aqui:
            menu_historia.render(imagens)
        if menu_opcoes.aqui:
            menu_opcoes.render(imagens)
        if menu_musicas.aqui:
            menu_musicas.render(imagens)

        pygame.display.update()


def tick():
    if menu_principal.aqui:
        menu_principal.tick(mudar_menu)
    if menu_escolha.aqui:
        menu_escolha.tick(mudar_menu)
    if menu_historia.aqui:
        menu_historia.tick(mudar_menu)
        menu_musicas.menu = menu_historia.menu
    if menu_opcoes.aqui:
        menu_opcoes.tick(mudar_menu)
    if menu_musicas.aqui:
        menu_musicas.tick(mudar_menu)

while tela.rodando:

    tick()
    render()

    r.tick(60)
