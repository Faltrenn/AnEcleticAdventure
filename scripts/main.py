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

        self.limitador_render = self.limitador_tick = self.FPS = 60
        self.antes_render = self.agora_render = self.antes_tick = self.agora_tick = time.time_ns()

        self.delta = 0

        self.telas = {"principal": Telas.MenuPrincipal(self)}

    def rodar(self):
        r = Thread(target=self.render)
        r.start()
        contador = ContadorFPS(self.FPS, "tick")
        self.antes_tick = time.time_ns()
        while self.tela.rodando:
            self.agora_tick = time.time_ns()
            self.delta = (self.agora_tick - self.antes_tick)/1000000000
            if self.delta >= 1/self.limitador_tick:
                self.antes_tick = self.agora_tick
                self.limitador_tick = contador.rodar()
                #Código
                for nome, menu in self.telas.items():
                    if menu.aqui:
                        menu.tick()

    def render(self):
        while self.tela.rodando:
            self.antes_tick = time.time_ns()
            contador = ContadorFPS(self.FPS, "render")
            while self.tela.rodando:
                self.agora_render = time.time_ns()
                delta = (self.agora_render - self.antes_render) / 1000000000
                if delta >= 1 / self.limitador_render:
                    self.antes_render = self.agora_render
                    self.limitador_render = contador.rodar()
                    # Código limitador = 60 fps = 56
                    for nome, menu in self.telas.items():
                        if menu.aqui:
                            if pygame.display.get_surface() is not None:
                                self.tela.janela.fill((255, 0, 0))
                                menu.render()
                                pygame.display.update()


class ContadorFPS:
    def __init__(self, FPS, lugar):
        self.limitador = self.FPS = FPS
        self.fps = self.antes = 0
        self.lugar = lugar

    def rodar(self):
        self.fps += 1
        if pygame.time.get_ticks() - self.antes >= 1000:
            self.antes += 1000
            print(f"FPS do {self.lugar}: {self.fps}")
            if self.fps != self.FPS:
                if self.fps < self.FPS:
                    self.limitador += 1
                if self.fps > self.FPS:
                    self.limitador -= 1
            self.fps = 0
        return self.limitador


main = Main()
main.rodar()
