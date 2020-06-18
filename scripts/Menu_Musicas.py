from scripts import Botoes
import pygame


class Menu_Musicas:
    def __init__(self, tela, fontes):
        self.nome = "menu_musicas"
        self.tela = tela
        self.fontes = fontes
        self.ctrl = self.w = False
        self.aqui = False
        self.menu = 0
        self.selecionado = 0
        self.bt_textos = ["Musica1", "Musica2", "Musica3", "Voltar"]
        self.bt_cores = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255)]
        self.bt_pos = [(150, 80), (150, 180), (150, 280), (150, 620)]
        self.botoes = Botoes.Botoes(fontes, self.bt_textos, self.bt_cores, self.bt_pos)

    def render(self, imagens):

        if self.menu == 0:
            self.bt_textos = ["Cantor1 - Musica1 P ", "Cantor2 - Musica2", "Cantor3 - Musica3", "Voltar"]
            self.botoes = Botoes.Botoes(self.fontes, self.bt_textos, self.bt_cores, self.bt_pos)


        if self.menu == 1:
            self.bt_textos = ["Cantor1 - Musica1 T ", "Cantor2 - Musica2", "Cantor3 - Musica3", "Voltar"]
            self.botoes = Botoes.Botoes(self.fontes, self.bt_textos, self.bt_cores, self.bt_pos)


        if self.menu == 2:
            self.bt_textos = ["Cantor1 - Musica1 E ", "Cantor2 - Musica2", "Cantor3 - Musica3", "Voltar"]
            self.botoes = Botoes.Botoes(self.fontes, self.bt_textos, self.bt_cores, self.bt_pos)


        self.tela.janela.blit(imagens.menu2_background, imagens.menu2_background.get_rect())

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
                    if e.key == pygame.K_DOWN:
                        if self.selecionado < 3:
                            self.selecionado += 1
                    if e.key == pygame.K_UP:
                        if self.selecionado > 0:
                            self.selecionado -= 1
                    if e.key == pygame.K_RETURN:
                        if self.selecionado == 3:
                            self.voltar(mudar_menu)
                            self.selecionado = 0

                # Tela solta
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = False
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = False

    def voltar(self, mudar_menu):
        mudar_menu.mudar_tela(self.nome, "menu_historia")
