import pygame
import arcade


class Tela:
    def __init__(self):
        self.rodando = True
        self.janela = pygame.display.set_mode((1280, 720))


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
        self.fonte_texto = pygame.font.Font("../src/fontes/Subspace.otf", 30)
        self.fonte_selec = pygame.font.Font("../src/fontes/Subspace Bold.otf", 50)


class Imagens:
    def __init__(self):
        self.imagens = {"back1": pygame.image.load("../src/imagens/background1.jpg").convert(),
                        "back2": pygame.image.load("../src/imagens/background2.jpg").convert(),
                        "back3": pygame.image.load("../src/imagens/background3.jpg").convert(),
                        "esteira1": pygame.image.load("../src/imagens/esteira1.jpg").convert()}


class Notas:
    def __init__(self, corda, tempo, velocidade):
        self.corda = corda
        self.cores = [(0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 0, 255)]
        self.posy = -15
        self.pos = [489 + (60 * self.corda) + self.corda - 1, self.posy]
        self.tempo = tempo
        self.velocidade = velocidade

    def tick(self, delta):
        self.posy += self.velocidade * delta
        self.pos[1] = int(self.posy)

    def render(self, tela):
        pygame.draw.circle(tela.janela, self.cores[self.corda-1], self.pos, 30)


class Gatilho:
    def __init__(self, corda, comando):
        self.comando = comando
        self.corda = corda + 1
        self.cores = [(0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 0, 255)]
        self.pos = [489 + (60 * self.corda) + self.corda - 1, 650]
        self.efetivo = True
        self.ativado = False
        self.inicio_ativ = 0
        self.notas = None

    def ativar(self, pressionado, notas):
        self.ativado = pressionado
        self.notas = notas

        if not pressionado:
            self.efetivo = True
        else:
            self.inicio_ativ = pygame.time.get_ticks()

    def tick(self):
        if self.ativado:
            if (pygame.time.get_ticks() - self.inicio_ativ)/1000 > 0.1:
                self.efetivo = False
            if self.efetivo:
                for nota in self.notas:
                    if 720 >= nota.posy >= 650 and nota.corda == self.corda:
                        self.notas.remove(nota)
                        self.efetivo = False

    def render(self, tela):
        pygame.draw.circle(tela.janela, self.cores[self.corda - 1], self.pos, 30, int(not self.ativado))


class Sons:
    def __init__(self):
        self.erro = arcade.Sound("../src/sons/som_erro.ogg")
