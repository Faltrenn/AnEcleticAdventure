from scripts import Botoes
import pygame


class Menu_Historia:
    def __init__(self, tela, fontes):
        self.nome = "menu_historia"
        self.fontes = fontes
        self.aqui = False
        self.tela = tela
        self.w = False
        self.ctrl = False
        self.selecionado = 0
        self.menu = 0
        self.bt_cores = [(0, 0, 0), (0, 0, 0,), (0, 0, 0), (255, 255, 255)]
        self.bt_textos = ["Thiago", "Lil Luvi", "Dj Bampa", "Voltar"]
        self.bt_pos = [(150, 80), (150, 180), (150, 280), (150, 620)]
        self.botoes = Botoes.Botoes(fontes, self.bt_textos, self.bt_cores, self.bt_pos)

    def render(self, imagens):
        self.tela.janela.blit(imagens.menu2_background, imagens.menu2_background.get_rect())

        self.botoes.render(self.selecionado, self.tela)

        if self.selecionado == 0:
            dimensoes = imagens.p1.get_rect()
            dimensoes[0] = 400
            dimensoes[1] = 50
            self.tela.janela.blit(imagens.p1, dimensoes)

            self.tela.janela.blit(self.fontes.fonte_biografia.render('Thiago é um pagodeiro moderno que ', True, (0, 0, 0)), (870, 80))
            self.tela.janela.blit(self.fontes.fonte_biografia.render('adora fazer um churrasco, vindo da', True, (0, 0, 0)), (870, 110))
            self.tela.janela.blit(self.fontes.fonte_biografia.render('periferia, seu sonho e ser um grande ', True, (0, 0, 0)), (870, 140))
            self.tela.janela.blit(self.fontes.fonte_biografia.render('cantor como seus idolos.', True, (0, 0, 0)), (870, 170))

        if self.selecionado == 1:
            dimensoes = imagens.p1.get_rect()
            dimensoes[0] = 400
            dimensoes[1] = 50

            self.tela.janela.blit(imagens.p1, dimensoes)

        if self.selecionado == 2:
            dimensoes = imagens.p1.get_rect()
            dimensoes[0] = 400
            dimensoes[1] = 50
            self.tela.janela.blit(imagens.p1, dimensoes)

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
                        if self.selecionado == 3:
                            self.voltar(mudar_menu)
                            self.selecionado = 0
                        if self.selecionado < 3:
                            self.menu = self.selecionado
                            self.selecionado = 0

                            self.menu_musicas(mudar_menu)

                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = False
                    if e.key == pygame.K_w:
                        self.w = False

    def voltar(self, mudar_menu):
        mudar_menu.mudar_tela(self.nome, "menu_escolha")

    def menu_musicas(self, mudar_menu):
        mudar_menu.mudar_tela(self.nome, "menu_musicas")

