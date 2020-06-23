from v2.scripts import Botoes
import pygame


class Menu_Escolha:
    def __init__(self, tela, fontes):
        self.nome = "menu_escolha"
        self.aqui = False
        self.tela = tela
        self.w = False
        self.ctrl = False
        self.selecionado = 0
        self.bt_cores = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255)]
        self.bt_textos = ["Modo História", "Online", "Outros", "Voltar"]
        self.bt_pos = [(150, 80), (150, 180), (150, 280), (150, 620)]
        self.botoes = Botoes.Botoes(fontes, self.bt_textos, self.bt_cores, self.bt_pos)

    def render(self, imagens):
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
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = True
                    if e.key == pygame.K_w:
                        self.w = True
                    if e.key == pygame.K_UP and self.selecionado > 0:
                        self.selecionado -= 1
                    if e.key == pygame.K_DOWN and self.selecionado < 3:
                        self.selecionado += 1
                    if e.key == pygame.K_RETURN:
                        if self.selecionado == 0:
                            self.modo_historia(mudar_menu)
                            
                        if self.selecionado == 3:
                            self.voltar(mudar_menu)
                            self.selecionado = 0

                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = False
                    if e.key == pygame.K_w:
                        self.w = False

    def voltar(self, mudar_menu):
        mudar_menu.mudar_tela(self.nome, "menu_principal")

    def modo_historia(self, mudar_menu):
        mudar_menu.mudar_tela(self.nome, "menu_historia")

