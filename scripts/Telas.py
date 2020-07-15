try:
    import Recursos
except ImportError:
    from scripts import Recursos
finally:
    import pygame


class TelaExemplo:
    def __init__(self, nome, infos, main, aqui=False):
        self.nome = nome
        self.aqui = aqui
        self.infos = infos
        self.botoes = Recursos.Botoes(infos)
        self.main = main

    def tick(self):
        self.botoes.tick(self.main.tela)

    def render(self):
        self.botoes.render(self.main.tela)

    def mudar_tela(self, sai_de, vai_para):
        self.__init__(self.main)
        self.main.telas[sai_de].aqui = False
        self.main.telas[vai_para].aqui = True


class MenuPrincipal(TelaExemplo):
    def __init__(self, main):
        self.infos = [["Jogar", (0, 0, 0), (400, 350), self.jogar],
                      ["Opções", (0, 0, 0), (600, 350), self.opcoes],
                      ["Sair", (255, 255, 255), (800, 350   ), self.sair]]
        super().__init__("principal", self.infos, main, True)


    def jogar(self):
        self.mudar_tela(self.nome, "jogar")


    def opcoes(self):
        self.mudar_tela(self.nome, "opcoes")

    def sair(self):
        self.main.tela.rodando = False
        pygame.quit()

class MenuJogar(TelaExemplo):
    def __init__(self, main):
        self.infos = [["Modo Historia", (0, 0, 0), (180, 80), self.historia],
                      ["Extras", (0, 0, 0), (180, 180), self.extras],
                      ["Online", (0, 0, 0), (180, 280), self.online],
                      ["Voltar", (255, 255, 255), (180, 600), self.voltar]]
        super().__init__("jogar", self.infos, main)


    def historia(self):
        self.mudar_tela(self.nome, "modo_historia")

    def extras(self):
        self.mudar_tela(self.nome, "extras")

    def online(self):
        self.mudar_tela(self.nome, "online")

    def voltar(self):
        self.mudar_tela(self.nome, "principal")

class MenuOpcoes(TelaExemplo):
    def __init__(self, main):
        self.infos = [["Voltar", (255, 255, 255), (600, 350), self.voltar]]

        super().__init__("opcoes", self.infos, main)

    def voltar(self):
        self.mudar_tela(self.nome, "principal")


class MenuModoHistoria(TelaExemplo):
    def __init__(self, main):
        self.infos = [["Voltar", (255, 255, 255), (600, 350), self.voltar]]

        super().__init__("modo_historia", self.infos, main)

    def voltar(self):
        self.mudar_tela(self.nome, "jogar")


class MenuExtras(TelaExemplo):
    def __init__(self, main):
        self.infos = [["Voltar", (255, 255, 255), (600, 350), self.voltar]]

        super().__init__("extras", self.infos, main)

    def voltar(self):
        self.mudar_tela(self.nome, "jogar")


class MenuOnline(TelaExemplo):
    def __init__(self, main):
        self.infos = [["Voltar", (255, 255, 255), (600, 350), self.voltar]]

        super().__init__("online", self.infos, main)

    def voltar(self):
        self.mudar_tela(self.nome, "jogar")