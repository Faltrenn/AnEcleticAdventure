try:
    import Telas
    import Recursos
except ImportError:
    from scripts import Telas, Recursos
finally:
    import pygame
    from threading import Thread
    import time
    import tkinter
    from tkinter import messagebox


pygame.init()


class Main:
    def __init__(self):
        self.tela = Recursos.Tela()

        self.erro = False

        self.r = None

        self.comandos = [pygame.K_a, pygame.K_s, pygame.K_j, pygame.K_k]
        try:
            self.telas = {"principal": Telas.MenuPrincipal(self, "back1"),
                          "jogar": Telas.MenuJogar(self, "back2"),
                          "opcoes": Telas.MenuOpcoes(self, "back1"),
                          "modo_historia": Telas.MenuModoHistoria(self, "back2"),
                          "extras": Telas.MenuExtras(self, "back2"),
                          "online": Telas.MenuOnline(self, "back2"),
                          "jogo": Telas.TelaJogar(self, "back2"),
                          "estatisticas": Telas.TelaEstatisticas(self, "back2")}
        except FileNotFoundError:
            self.deu_erro()

    def deu_erro(self):
        self.tela.rodando = False
        self.erro = True
        tk = tkinter.Tk()
        tk.withdraw()
        messagebox.showerror("Seu safadinho/a", "Apagou alguma coisa aí seu vacilão!")

    def rodar(self):
        self.r = Thread(target=self.render)
        self.r.start()
        antes = time.time_ns()
        while self.tela.rodando:
            if self.erro:
                return
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
            if self.erro:
                return
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
