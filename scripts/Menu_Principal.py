from scripts import Botoes
import pygame


class Menu_Principal:
    def __init__(self, tela, fontes):
        self.nome = "menu_principal"
        self.tela = tela
        self.ctrl = self.w = False
        self.aqui = True
        self.selecionado = 0
        self.bt_textos = ["Jogar", "Opções", "Sair"]
        self.bt_cores = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
        self.bt_pos = [(300, 600), (600, 600), (900, 600)]
        self.botoes = Botoes.Botoes(fontes, self.bt_textos, self.bt_cores, self.bt_pos)

    def render(self, imagens):
        self.tela.janela.blit(imagens.menu_background, imagens.menu_background.get_rect())

        self.botoes.render(self.selecionado, self.tela)

    def tick(self, mudar_menu):
        if self.w and self.ctrl:
            pygame.quit()
            self.tela.rodando = False
        if pygame.display.get_surface() is not None:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    self.tela.rodando = False
                # Tela pressionada
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = True
                    if e.key == pygame.K_w:
                        self.w = True
                    if e.key == pygame.K_UP:
                        if self.selecionado < 2:
                            self.selecionado += 1
                    if e.key == pygame.K_DOWN:
                        if self.selecionado > 0:
                            self.selecionado -= 1
                    if e.key == pygame.K_RETURN:
                        if self.selecionado == 0:
                            self.jogar(mudar_menu)
                        if self.selecionado == 1:
                            self.opcoes()
                        if self.selecionado == 2:
                            self.sair()
                # Tela solta
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = False
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = False

    def jogar(self, mudar_menu):
        mudar_menu.mudar_tela(self.nome, "menu_escolha")

    def opcoes(self):
        print("Abre as opcoes")

    def sair(self):
        pygame.quit()
        self.tela.rodando = False
