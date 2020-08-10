import pygame


class Tela:
    def __init__(self):
        self.rodando = True
        self.janela = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)


class Botoes:
    def __init__(self, infos):# [[nome, cor, posicao, acao]]
        self.textos = list()
        self.cores = list()
        self.posicoes = list()
        self.acoes = list()
        for info in infos:
            self.textos.append(info[0])
            self.cores.append(info[1])
            self.posicoes.append(info[2])
            self.acoes.append(info[3])

        self.botoes = list()
        self.fontes = Fontes()
        self.selec = 0
        for c in range(0, len(infos)):
            self.botoes.append([self.fontes.fonte_normal.render(self.textos[c], True, self.cores[c]), False])

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
                    self.acoes[self.selec]()

        for c, botao in enumerate(self.botoes):
            if c == self.selec and not botao[1]:
                self.botoes[self.selec] = [self.fontes.fonte_selec.render(self.textos[self.selec], True, self.cores[self.selec]), True]
            elif c != self.selec and botao[1]:
                self.botoes[c] = [self.fontes.fonte_normal.render(self.textos[c], True, self.cores[c]), False]

    def render(self, tela):
        for c, botao in enumerate(self.botoes):
            tela.janela.blit(botao[0], self.posicoes[c])


class Fontes:
    def __init__(self):
        self.fonte_normal = pygame.font.Font("../src/fontes/Subspace.otf", 40)
        self.fonte_selec = pygame.font.Font("../src/fontes/Subspace Bold.otf", 50)


class Imagens:
    def __init__(self):
        self.imagens = {"back1": pygame.image.load("../src/imagens/background1.jpg").convert(),
                        "back2": pygame.image.load("../src/imagens/background2.jpg").convert(),
                        "back3": pygame.image.load("../src/imagens/background3.jpg").convert()}
