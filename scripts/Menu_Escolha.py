import pygame


class Menu_Escolha:
    def __init__(self, tela, fontes):
        self.menu_escolha = False
        self.tela = tela
        self.w = False
        self.ctrl = False
        self.selecionado = 0
        self.fontes = fontes
        self.txt_personagem1 = self.fontes.fonte.render("Thiago", True, (0, 0, 0))
        self.txt_personagem2 = self.fontes.fonte.render("Lil Luvi", True, (0, 0, 0))
        self.txt_personagem3 = self.fontes.fonte.render("Dj Bampa", True, (0, 0, 0))
        self.txt_online = self.fontes.fonte.render("Online", True, (0, 0, 0))
        self.txt_outros = self.fontes.fonte.render("Outros", True, (0, 0, 0))
        self.txt_voltar = self.fontes.fonte.render("Voltar", True, (0, 0, 0))
        self.textos = ["Thiago", "Lil Luvi", "Dj Bampa", "Online", "Outros", "Voltar"]
        self.botoes = []

    def render(self, imagens):
        self.tela.janela.blit(imagens.menu2_background, imagens.menu2_background.get_rect())

        self.botoes = [[self.txt_personagem1, (150, 80)],
                       [self.txt_personagem2, (150, 180)],
                       [self.txt_personagem3, (150, 280)],
                       [self.txt_online, (150, 380)],
                       [self.txt_outros, (150, 480)],
                       [self.txt_voltar, (150, 620)]]

        self.botoes[self.selecionado][0] = self.fontes.fonte_selecionado.render(self.textos[self.selecionado], True, (0, 0, 0))

        for botao in self.botoes:
            self.tela.janela.blit(botao[0], botao[1])

    def tick(self):
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
                    if e.key == pygame.K_DOWN and self.selecionado < 5:
                        self.selecionado += 1
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LCTRL:
                        self.ctrl = False
                    if e.key == pygame.K_w:
                        self.w = False
