try:
    import Recursos
except ImportError:
    from scripts import Recursos
finally:
    import pygame


class TelaExemplo:
    def __init__(self, nome, infos, main, back, aqui=False):
        self.tela_anterior = ""
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
        self.main.telas[vai_para].tela_anterior = sai_de


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


class TelaEstatisticas(TelaExemplo):
    def __init__(self, main, back):
        self.infos = [["Voltar", (255, 255, 255), (600, 550), self.voltar]]
        self.fontes = Recursos.Fontes()
        self.textos = [["Nome da Música: ", (0, 0, 0), (150, 60)],
                       ["Score: ", (0, 0, 0), (150, 160)],
                       ["Porcentagem de Acerto: ", (0, 0, 0), (150, 260)],
                       ["Acertos: ", (0, 0, 0), (150, 360)]]
        self.estatisticas = list()
        super().__init__("estatisticas", self.infos, main, back)

    def voltar(self):
        self.mudar_tela(self.nome, self.main.telas["jogo"].tela_anterior)
        self.main.telas["jogo"].__init__(self.main, self.back)

    def render(self):
        self.main.tela.janela.blit(self.imagens.imagens[self.back],
                                   self.imagens.imagens[self.back].get_rect())
        for c, texto in enumerate(self.estatisticas):
            self.main.tela.janela.blit(texto, self.textos[c][2])
        self.botoes.render(self.main.tela)

    def carregar_estatisticas(self, obj):
        self.textos[0][0] += obj.nome_musica
        self.textos[1][0] += str(obj.score)
        self.textos[2][0] += str((obj.acertos * 100)/obj.quant_notas) + "%"
        self.textos[3][0] += str(obj.acertos)
        for texto in self.textos:
            self.estatisticas.append(self.fontes.fonte_texto.render(texto[0], True, texto[1]))


class TelaJogar:
    def __init__(self, main, back):
        self.aqui = False
        self.tela_anterior = ""
        self.main = main
        self.nome = "jogo"
        self.back = back
        self.imagens = Recursos.Imagens()

        # Notas
        self.notas_provisorias = list()
        self.notas_esteira = list()
        self.notas_carregadas = False
        self.agora = 0

        # Musica
        self.musica = None

        # Gatilhos
        self.gatilho1 = Recursos.Gatilho(0, self.main.comandos[0])
        self.gatilho2 = Recursos.Gatilho(1, self.main.comandos[1])
        self.gatilho3 = Recursos.Gatilho(2, self.main.comandos[2])
        self.gatilho4 = Recursos.Gatilho(3, self.main.comandos[3])

    def tick(self, delta):
        if self.notas_carregadas:
            # Tempo desde que carregou a musica
            tempo = (pygame.time.get_ticks() - self.agora)/1000

            # Colocando notas na tela no tempo delas
            for nota in self.notas_provisorias:
                if nota.tempo <= tempo:
                    self.notas_esteira.append(nota)
                    self.notas_provisorias.remove(nota)

            # Fazendo as notas descerem
            for nota in self.notas_esteira:
                nota.tick(delta)

            # Teste

            if tempo > 25:
                self.imagens.imagens["esteira2fade1"].set_alpha(0)

            print(tempo)



        self.gatilho1.tick()
        self.gatilho2.tick()
        self.gatilho3.tick()
        self.gatilho4.tick()

        # Verificando se os gatilhos estão pressionados
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == self.gatilho1.comando:
                    self.gatilho1.ativar(True, self.notas_esteira)
                if e.key == self.gatilho2.comando:
                    self.gatilho2.ativar(True, self.notas_esteira)
                if e.key == self.gatilho3.comando:
                    self.gatilho3.ativar(True, self.notas_esteira)
                if e.key == self.gatilho4.comando:
                    self.gatilho4.ativar(True, self.notas_esteira)
            if e.type == pygame.KEYUP:
                if e.key == self.gatilho1.comando:
                    self.gatilho1.ativar(False, self.notas_esteira)
                if e.key == self.gatilho2.comando:
                    self.gatilho2.ativar(False, self.notas_esteira)
                if e.key == self.gatilho3.comando:
                    self.gatilho3.ativar(False, self.notas_esteira)
                if e.key == self.gatilho4.comando:
                    self.gatilho4.ativar(False, self.notas_esteira)

            if e.type == pygame.QUIT:
                self.main.tela.rodando = False
                pygame.quit()


    def render(self):


        self.main.tela.janela.blit(self.imagens.imagens[self.back],
                                   self.imagens.imagens[self.back].get_rect())

        self.main.tela.janela.blit(self.imagens.imagens["esteira2fade2"], (518, 0, 244, 720))

        self.main.tela.janela.blit(self.imagens.imagens["esteira2fade1"], (518, 0, 244, 720))




        for nota in self.notas_esteira:
            nota.render(self.main.tela)

        self.gatilho1.render(self.main.tela)
        self.gatilho2.render(self.main.tela)
        self.gatilho3.render(self.main.tela)
        self.gatilho4.render(self.main.tela)

    def mudar_tela(self, sai_de, vai_para):
        self.main.telas[sai_de].__init__(self.main, self.back)
        self.main.telas[sai_de].aqui = False
        self.main.telas[vai_para].aqui = True
        self.main.telas[vai_para].tela_anterior = sai_de

    def carregar_musica(self, nome_musica, velocidade):
        arquivo = open("../src/musicas/"+nome_musica+".txt", "r")
        for linha in arquivo:
            for c, caractere in enumerate(linha):
                if c <= 8 and caractere.isdigit() and caractere != "0":
                    self.notas_provisorias.append(Recursos.Notas(int(caractere), float(linha[9:]), velocidade))
        self.musica = pygame.mixer.music.load("../src/musicas/"+nome_musica+".ogg")
        self.agora = pygame.time.get_ticks()
        self.notas_carregadas = True

