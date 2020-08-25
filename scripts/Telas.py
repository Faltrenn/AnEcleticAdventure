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
        self.botoes = [[(549, 640), (0, 255, 0), False],
                       [(610, 640), (255, 0, 0), False],
                       [(671, 640), (255, 255, 0), False],
                       [(732, 640), (0, 0, 255), False]]

        self.nome_musica = ""
        self.musica = None
        self.tocando = False
        self.quant_notas = 0
        # Adicionar Notas
        self.notas_provisorias = list()
        self.notas_na_esteira = list()
        self.notas_carregadas = False
        self.agora = self.antes = pygame.time.get_ticks()
        self.tempo = 0

        # Estatísticas
        self.sequencia = self.acertos = self.score = 0
        self.mult_score = 1

        self.satisfacao = 6
        self.cores_satisfacao = ((255, 0, 0), (255, 255, 0), (0, 255, 0))
        self.cor_atual = 0

        self.fontes = Recursos.Fontes()
        self.textos = [[self.fontes.fonte_texto.render("Score: " + str(self.score), True, (0, 0, 0)), (900, 550)],
                       [self.fontes.fonte_texto.render("Multiplicador" + str(self.mult_score), True, (0, 0, 0)), (1000, 550)]]

        # Efeitos sonoros
        self.sons = Recursos.Sons()

    def tick(self, delta):
        keys = pygame.key.get_pressed()
        for c, botao in enumerate(self.botoes):
            self.botoes[c][2] = keys[self.main.comandos[c]]

        if self.notas_carregadas:
            self.agora = pygame.time.get_ticks()
            self.tempo = self.agora - self.antes
            if not self.tocando:
                self.musica.set_volume(0.15)
                self.musica.play()
                self.tocando = True
            # Adicionando notas na tela
            for nota in self.notas_provisorias:
                if nota.tempo <= self.tempo / 1000:
                    self.notas_na_esteira.append(nota)
                    self.notas_provisorias.remove(nota)
            self.mult_score = int(self.sequencia / 20) + 1
            for nota in self.notas_na_esteira:
                nota.tick(delta)
                for botao in self.botoes:
                    # Verificando colisões
                    if botao[2] and (botao[0][1] - 20) <= nota.pos[1] <= (botao[0][1] + 20) and botao[0][0] == nota.pos[0]:
                        self.notas_na_esteira.remove(nota)
                        self.acertos += 1
                        self.sequencia += 1
                        self.score += 1 * self.mult_score
                        if self.satisfacao < 12:
                            self.satisfacao += 1
                    elif botao[2]:
                        self.sons.erro.play()
                        self.sequencia = 0
                        self.satisfacao -= 1
                        self.mult_score = 1

                # Nota saindo da tela
                if nota.pos[1] >= 735:
                    self.notas_na_esteira.remove(nota)
                    self.mult_score = 1
                    self.sequencia = 0
                    if self.satisfacao > 1:
                        self.satisfacao -= 1
                    # else:
                    #     self.mudar_tela(self.nome, "estatisticas")

            for botao in self.botoes:
                if botao[2] and len(self.notas_na_esteira) == 0:
                    self.sons.erro.play()
                    self.sequencia = 0
                    self.satisfacao -= 1
                    self.mult_score = 1

            if self.satisfacao <= 4:
                self.cor_atual = self.cores_satisfacao[0]
            elif self.satisfacao <= 8:
                self.cor_atual = self.cores_satisfacao[1]
            else:
                self.cor_atual = self.cores_satisfacao[2]
            self.textos = [[self.fontes.fonte_texto.render("Score: " + str(self.score), True, (0, 0, 0)), (850, 400)],
                           [self.fontes.fonte_texto.render("Multiplicador: " + str(self.mult_score), True, (0, 0, 0)), (1000, 400)]]

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
        pygame.draw.rect(self.main.tela.janela, self.cor_atual, ((1100, 570), (100, 100)))
        for texto in self.textos:
            self.main.tela.janela.blit(texto[0], texto[1])

    def carregar_musica(self, nome, velocidade):
        self.nome_musica = nome
        try:
            self.musica = pygame.mixer.Sound("../src/musicas/" + nome + ".ogg")
            arquivo = open("../src/musicas/" + nome + ".txt", "r")
            for linha in arquivo:
                for c, caractere in enumerate(linha):
                    if c <= 8 and caractere.isdigit() and caractere != "0":
                        self.notas_provisorias.append(Recursos.Notas(int(caractere), float(linha[9:-1]), velocidade))
        except FileNotFoundError:
            self.main.deu_erro()

        self.quant_notas = len(self.notas_provisorias)
        self.antes = self.agora = pygame.time.get_ticks()
        self.tempo = 0
        self.notas_carregadas = True

    def mudar_tela(self, sai_de, vai_para):
        self.main.telas["estatisticas"].carregar_estatisticas(self)
        self.musica.stop()
        self.main.telas[sai_de].aqui = False
        self.main.telas[vai_para].aqui = True

