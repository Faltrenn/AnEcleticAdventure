try:
    import Recursos
except ImportError:
    from scripts import Recursos
finally:
    import pygame


class TelaExemplo:
    def __init__(self, nome, infos, main, back, aqui=False):
        self.nome = nome
        self.aqui = aqui
        self.infos = infos
        self.botoes = Recursos.Botoes(infos)
        self.imagens = Recursos.Imagens()
        self.back = back
        self.main = main

    def tick(self):
        self.botoes.tick(self.main.tela)

    def render(self):
        self.main.tela.janela.blit(self.imagens.imagens[self.back],
                                   self.imagens.imagens[self.back].get_rect())
        self.botoes.render(self.main.tela)

    def mudar_tela(self, sai_de, vai_para):
        self.__init__(self.main, self.back)
        self.main.telas[sai_de].aqui = False
        self.main.telas[vai_para].aqui = True


class MenuPrincipal(TelaExemplo):
    def __init__(self, main, back):
        self.infos = [["Jogar", (0, 0, 0), (400, 350), self.jogar],
                      ["Opções", (0, 0, 0), (600, 350), self.opcoes],
                      ["Sair", (255, 255, 255), (800, 350), self.sair]]
        super().__init__("principal", self.infos, main, back, True)

    def jogar(self):
        self.mudar_tela(self.nome, "jogar")

    def opcoes(self):
        self.mudar_tela(self.nome, "opcoes")

    def sair(self):
        self.main.tela.rodando = False
        pygame.quit()


class MenuJogar(TelaExemplo):
    def __init__(self, main, back):
        self.infos = [["Modo Historia", (0, 0, 0), (180, 80), self.historia],
                      ["Extras", (0, 0, 0), (180, 180), self.extras],
                      ["Online", (0, 0, 0), (180, 280), self.online],
                      ["Voltar", (255, 255, 255), (180, 600), self.voltar]]
        super().__init__("jogar", self.infos, main, back)

    def historia(self):
        self.mudar_tela(self.nome, "modo_historia")

    def extras(self):
        self.mudar_tela(self.nome, "extras")

    def online(self):
        self.mudar_tela(self.nome, "online")

    def voltar(self):
        self.mudar_tela(self.nome, "principal")


class MenuOpcoes(TelaExemplo):
    def __init__(self, main, back):
        self.infos = [["Voltar", (255, 255, 255), (600, 350), self.voltar]]

        super().__init__("opcoes", self.infos, main, back)

    def voltar(self):
        self.mudar_tela(self.nome, "principal")


class MenuModoHistoria(TelaExemplo):
    def __init__(self, main, back):
        self.infos = [["Voltar", (255, 255, 255), (600, 350), self.voltar]]

        super().__init__("modo_historia", self.infos, main, back)

    def voltar(self):
        self.mudar_tela(self.nome, "jogar")


class MenuExtras(TelaExemplo):
    def __init__(self, main, back):
        self.infos = [["Naruto sad", (0, 0, 0), (180, 80), self.NarutoSad],
                      ["Voltar", (255, 255, 255), (180, 600), self.voltar]]

        super().__init__("extras", self.infos, main, back)

    def NarutoSad(self):
        self.main.telas["jogo"].carregar_musica("Musica1", 240)
        self.mudar_tela(self.nome, "jogo")

    def voltar(self):
        self.mudar_tela(self.nome, "jogar")


class MenuOnline(TelaExemplo):
    def __init__(self, main, back):
        self.infos = [["Voltar", (255, 255, 255), (600, 350), self.voltar]]

        super().__init__("online", self.infos, main, back)

    def voltar(self):
        self.mudar_tela(self.nome, "jogar")


class TelaJogar:
    def __init__(self, main, back):
        self.aqui = False
        self.main = main
        self.nome = "jogo"
        self.back = back
        self.imagens = Recursos.Imagens()
        self.botoes = [[(549, 640), (0, 255, 0), False],
                       [(610, 640), (255, 0, 0), False],
                       [(671, 640), (255, 255, 0), False],
                       [(732, 640), (0, 0, 255), False]]

        # Adicionar Notas
        self.notas_provisorias = list()
        self.notas_na_esteira = list()
        self.notas_carregadas = False
        self.agora = self.antes = pygame.time.get_ticks()
        self.tempo = 0

    def tick(self, delta):
        keys = pygame.key.get_pressed()
        for c, botao in enumerate(self.botoes):
            self.botoes[c][2] = keys[self.main.comandos[c]]

        if self.notas_carregadas:
            self.agora = pygame.time.get_ticks()
            self.tempo = self.agora - self.antes
            for nota in self.notas_provisorias:
                if nota.tempo <= self.tempo / 1000:
                    self.notas_na_esteira.append(nota)
                    self.notas_provisorias.remove(nota)
            for nota in self.notas_na_esteira:
                nota.tick(delta)
                for botao in self.botoes:
                    if botao[2] and (botao[0][1] - 20) <= nota.pos[1] <= (botao[0][1] + 20) and botao[0][0] == nota.pos[0]:
                        self.notas_na_esteira.remove(nota)
                if nota.pos[1] >= 735:
                    self.notas_na_esteira.remove(nota)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.main.tela.rodando = False
                pygame.quit()

    def render(self):
        self.main.tela.janela.blit(self.imagens.imagens[self.back],
                                   self.imagens.imagens[self.back].get_rect())
        pygame.draw.rect(self.main.tela.janela, (255, 255, 255), ((519, 0), (244, 720))) #Esteira
        for botao in self.botoes:
            pygame.draw.circle(self.main.tela.janela, botao[1], botao[0], 30, int(not botao[2]))
        for nota in self.notas_na_esteira:
            nota.render(self.main.tela)

    def carregar_musica(self, nome, velocidade):
        arquivo = open("../src/musicas/" + nome + ".txt", "r")
        for linha in arquivo:
            for c, caractere in enumerate(linha):
                if c <= 8 and caractere.isdigit() and caractere != "0":
                    self.notas_provisorias.append(Recursos.Notas(int(caractere), float(linha[9:-1]), velocidade))
        self.antes = self.agora = pygame.time.get_ticks()
        self.tempo = 0
        self.notas_carregadas = True

    def mudar_tela(self, sai_de, vai_para):
        self.__init__(self.main, self.back)
        self.main.telas[sai_de].aqui = False
        self.main.telas[vai_para].aqui = True

