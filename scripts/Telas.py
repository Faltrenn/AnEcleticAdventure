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
        self.botoes = Recursos.Botoes(infos)
        self.main = main

    def tick(self):
        self.botoes.tick(self.main.tela)

    def render(self):
        self.botoes.render(self.main.tela)

    def mudar_tela(self, sai_de, vai_para):
        self.main.telas[sai_de].aqui = False
        self.main.telas[vai_para].aqui = True


class MenuPrincipal(TelaExemplo):
    def __init__(self, main):
        self.infos = [["Jogar", (0, 0, 0), (300, 300), self.jogar],
                      ["Opções", (0, 0, 0), (550, 300), self.opcoes],
                      ["Sair", (255, 255, 255), (800, 300), self.sair]]
        super().__init__("principal", self.infos, main, True)

    def jogar(self):
        pass

    def opcoes(self):
        pass

    def sair(self):
        self.main.tela.rodando = False
        pygame.quit()
