import pygame


class Menu_Opcoes:
    def __init__(self, tela, fontes):
        self.nome = "menu_opcoes"
        self.aqui = False
        self.tela = tela
        self.w = False
        self.ctrl = False
        self.selecionado = 0
        self.fontes = fontes
        self.btn_controleNormal = self.fontes.fonte.render("Thiago", True, (0, 0, 0))
        self.btn_controlePalhetar = self.fontes.fonte.render("Lil Luvi", True, (0, 0, 0))
        self.btn_p3 = self.fontes.fonte.render("Dj Bampa", True, (0, 0, 0))
        self.btn_voltar = self.fontes.fonte.render("Voltar", True, (255, 255, 255))
        self.textos = ["Thiago", "Lil Luvi", "Dj Bampa", "Voltar"]
        self.botoes = []
        self.cores = [(0, 0, 0), (0, 0, 0,), (0, 0, 0), (255, 255, 255)]

    def render(self, imagens):
        self.tela.janela.blit(imagens.menu2_background, imagens.menu2_background.get_rect())

        self.botoes = [[self.btn_p1, (150, 80)],
                       [self.btn_p2, (150, 180)],
                       [self.btn_p3, (150, 280)],
                       [self.btn_voltar, (150, 620)]]

        self.botoes[self.selecionado][0] = self.fontes.fonte_selecionado.render(self.textos[self.selecionado], True, self.cores[self.selecionado])

        for botao in self.botoes:
            self.tela.janela.blit(botao[0], botao[1])

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
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = False
                    if e.key == pygame.K_w:
                        self.w = False

    def voltar(self, mudar_menu):
        mudar_menu.mudar_tela(self.nome, "menu_principal")

