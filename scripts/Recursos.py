import pygame


class Tela:
    def __init__(self):
        self.rodando = True
        self.janela = pygame.display.set_mode((1280, 720))


class Botoes:
    def __init__(self, infos):
        self.infos = infos
        self.botoes = list()
        self.fontes = Fontes()
        self.selec = 0
        for info in self.infos:
            self.botoes.append([self.fontes.fonte_normal.render(info[0], True, info[1]), False])

    def tick(self, tela):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                tela.rodando = False
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP and self.selec > 0:
                    self.selec -= 1
                if e.key == pygame.K_DOWN and self.selec < len(self.botoes) - 1:
                    self.selec += 1
                if e.key == pygame.K_RETURN:
                    self.infos[self.selec][3]()

        for c, botao in enumerate(self.botoes):
            if not botao[1] and c == self.selec:
                self.botoes[c] = [self.fontes.fonte_selec.render(self.infos[c][0], True,
                                                                 self.infos[c][1]), True]
            if self.botoes[1] and c != self.selec:
                self.botoes[c] = [self.fontes.fonte_normal.render(self.infos[c][0], True,
                                                                  self.infos[c][1]), False]

    def render(self, tela):
        for c, botao in enumerate(self.botoes):
            tela.janela.blit(botao[0], self.infos[c][2])


class Fontes:
    def __init__(self):
        self.fonte_normal = pygame.font.Font("../src/fontes/Subspace.otf", 40)
        self.fonte_selec = pygame.font.Font("../src/fontes/Subspace Bold.otf", 50)