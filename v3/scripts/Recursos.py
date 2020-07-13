import pygame


class Tela:
    def __init__(self):
        self.rodando = True
        self.width = 1280
        self.height = 720
        self.janela = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Dale no joguinho")
        self.volume = 0.1

        self.ctrl = self.w = False

    def tick(self, COMANDOS, mudar_tela, main):
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (self.ctrl and self.w):
                self.rodando = False
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LCTRL:
                    self.ctrl = True
                if e.key == pygame.K_w:
                    self.w = True
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LCTRL:
                    self.ctrl = False
                if e.key == pygame.K_w:
                    self.w = False
            COMANDOS[0](e, mudar_tela, self, main)


class Imagens:
    def __init__(self):
        self.back_menu_principal = pygame.image.load("../src/imagens/menu_background.jpg").convert()
        self.back_menu2 = pygame.image.load("../src/imagens/menu2_background.jpg").convert()
        self.back_menu_wip = pygame.image.load("../src/imagens/menu_wip.jpg").convert()


class Fontes:
    def __init__(self):
        self.fonte_bt_normal = pygame.font.Font("../src/fontes/Subspace.otf", 40)
        self.fonte_bt_selec = pygame.font.Font("../src/fontes/Subspace Bold.otf", 50)


class Botoes:
    def __init__(self, infos):
        self.fontes = Fontes()
        self.infos = infos
        self.botoes = list()
        self.selec = 0

    def rodar(self, tela):
        self.botoes = []
        for info in self.infos:
            self.botoes.append(self.fontes.fonte_bt_normal.render(info[0], True, info[1]))
        self.botoes[self.selec] = self.fontes.fonte_bt_selec.render(self.infos[self.selec][0], True,
                                                                    self.infos[self.selec][1])
        for c, bt in enumerate(self.botoes):
            tela.janela.blit(bt, self.infos[c][2])

    def comandos(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                if self.selec > 0:
                    self.selec -= 1
            if e.key == pygame.K_DOWN:
                if self.selec < len(self.infos) - 1:
                    self.selec += 1


class Mensagem:
    def __init__(self):
        pass


class Notas:
    def __init__(self, corda, tempo):
        self.corda = corda
        self.tempo = tempo

    def rodar(self):
        pass
