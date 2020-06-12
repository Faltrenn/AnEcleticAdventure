import pygame


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.ctrl = self.w = False
        self.no_menu = True
        self.selecionado = 0
        self.font = pygame.font.Font("../fonte/Subspace.otf", 40)
        self.font_selecionado = pygame.font.Font("../fonte/Subspace Bold.otf", 50)
        self.txt_jogar = self.font.render("Jogar", True, (0, 0, 0))
        self.txt_opcoes = self.font.render("Opções", True, (0, 0, 0))
        self.txt_sair = self.font.render("Sair", True, (0, 0, 0))
        self.textos = ["Jogar", "Opções", "Sair"]
        self.botoes = [[self.txt_jogar, (300, 600)], [self.txt_opcoes, (600, 600)], [self.txt_sair, (900, 600)]]

    def render(self, imagens):
        self.tela.janela.blit(imagens.menu_background, imagens.menu_background.get_rect())

        self.botoes = [[self.txt_jogar, (300, 600)], [self.txt_opcoes, (600, 600)], [self.txt_sair, (900, 600)]]
        self.botoes[self.selecionado][0] = self.font_selecionado.render(self.textos[self.selecionado], True, (0, 0, 0))

        for botao in self.botoes:
            self.tela.janela.blit(botao[0], botao[1])

    def tick(self, menu_escolha):
        if self.w and self.ctrl:
            pygame.quit()
            self.tela.rodando = False
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
                        self.jogar(menu_escolha)
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

    def jogar(self, menu_escolha):
        menu_escolha.menu_escolha = True
        self.no_menu = False

    def opcoes(self):
        print("Abre as opcoes")

    def sair(self):
        pygame.quit()
        self.tela.rodando = False
