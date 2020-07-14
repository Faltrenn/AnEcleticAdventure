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
        fps = antes = 0
        self.antes_tick = time.time_ns()
        while self.tela.rodando:
            self.agora_tick = time.time_ns()
            self.delta = (self.agora_tick - self.antes_tick)/1000000000
            if self.delta >= 1/self.limitador_tick:
                self.antes_tick = self.agora_tick
                fps += 1
                if pygame.time.get_ticks() - antes >= 1000:
                    antes += 1000
                    if fps != self.FPS:
                        if fps < self.FPS:
                            self.limitador_tick += 1
                        else:
                            self.limitador_tick -= 1
                    print(f"FPS do tick: {fps}")
                    fps = 0
                #Código
                for nome, menu in self.telas.items():
                    if menu.aqui:
                        menu.tick()

    def render(self):
        while self.tela.rodando:
            fps = antes = 0
            self.antes_tick = time.time_ns()
            while self.tela.rodando:
                self.agora_render = time.time_ns()
                delta = (self.agora_render - self.antes_render) / 1000000000
                if delta >= 1 / self.limitador_render:
                    self.antes_render = self.agora_render
                    fps += 1
                    if pygame.time.get_ticks() - antes >= 1000:
                        antes += 1000
                        if fps != self.FPS:
                            if fps < self.FPS:
                                self.limitador_render += 1
                            else:
                                self.limitador_render -= 1
                        print(f"FPS do render: {fps}")
                        fps = 0
                    # Código
                    for nome, menu in self.telas.items():
                        if menu.aqui:
                            if pygame.display.get_surface() is not None:
                                self.tela.janela.fill((255, 0, 0))
                                menu.render()
                                pygame.display.update()


main = Main()
main.rodar()
