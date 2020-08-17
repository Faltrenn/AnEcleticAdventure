try:
    import Telas
    import Recursos
except ImportError:
    from scripts import Telas, Recursos
finally:
    import pygame
    from threading import Thread
    import time


pygame.init()


class Main:
    def __init__(self):
        self.tela = Recursos.Tela()

        self.comandos = [pygame.K_a, pygame.K_s, pygame.K_j, pygame.K_k]

        self.telas = {"principal": Telas.MenuPrincipal(self, "back1"),
                      "jogar": Telas.MenuJogar(self, "back2"),
                      "opcoes": Telas.MenuOpcoes(self, "back1"),
                      "modo_historia": Telas.MenuModoHistoria(self, "back2"),
                      "extras": Telas.MenuExtras(self, "back2"),
                      "online": Telas.MenuOnline(self, "back2"),
                      "jogo": Telas.TelaJogar(self, "back2"),
                      "estatisticas": Telas.TelaEstatisticas(self, "back2")}

    def rodar(self):
        r = Thread(target=self.render)
        r.start()
        antes = time.time_ns()
        while self.tela.rodando:
            agora = time.time_ns()
            delta = (agora - antes)/1000000000
            antes = agora
            #Código
            for nome, menu in self.telas.items():
                if menu.aqui:
                    if menu.nome == "jogo":
                        menu.tick(delta)
                    else:
                        menu.tick()

    def render(self):
        while self.tela.rodando:
            while self.tela.rodando:
                # Código limitador
                for nome, menu in self.telas.items():
                    if menu.aqui:
                        if pygame.display.get_surface() is not None:
                            self.tela.janela.fill((255, 0, 0))
                            menu.render()
                            pygame.display.update()


main = Main()
main.rodar()
