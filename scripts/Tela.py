import pygame
from scripts import Player, Notas

pygame.init()


class Tela:

    def __init__(self):
        self.janela = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        self.notas = []
        self.rodando = True
        self.ctrl = False
        self.kw = False
        self.fps = 0
        self.antes = 0
        self.player = Player.Player()

    def render(self):
        self.fps = self.fps + 1
        if pygame.time.get_ticks() - self.antes >= 1000:
            self.antes = pygame.time.get_ticks()
            print(self.fps)
            self.fps = 0
        self.janela.fill((255, 255, 255))
        for nota in self.notas:
            nota.render(self.janela)
            nota.tick(self, self.player)

        self.player.render(self.janela)
        self.player.tick()

        pygame.display.update()

    def fechar(self):
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT or self.ctrl and self.kw:
                pygame.quit()
                self.rodando = False
                
            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_w:
                    self.kw = True
                if eventos.key == pygame.K_LCTRL:
                    self.ctrl = True
                # INTERAÇÕES DO USUÁRIO

                if eventos.key == pygame.K_CAPSLOCK:
                    if self.player.modo == "palhetar":
                        self.player.modo = "normal"
                    else:
                        self.player.modo = "palhetar"

                if self.player.modo == "normal":
                    if eventos.key == pygame.K_a:
                        self.player.btn1 = 0
                    if eventos.key == pygame.K_s:
                        self.player.btn2 = 0
                    if eventos.key == pygame.K_j:
                        self.player.btn3 = 0
                    if eventos.key == pygame.K_k:
                        self.player.btn4 = 0
                elif self.player.modo == "palhetar":
                    if eventos.key == pygame.K_F1:
                        self.player.f1 = True
                    if eventos.key == pygame.K_F2:
                        self.player.f2 = True
                    if eventos.key == pygame.K_F3:
                        self.player.f3 = True
                    if eventos.key == pygame.K_F4:
                        self.player.f4 = True
                    if eventos.key == pygame.K_UP:
                        self.player.cima = True
                    if eventos.key == pygame.K_DOWN:
                        self.player.baixo = True
            elif eventos.type == pygame.KEYUP:
                if eventos.key == pygame.K_w:
                    self.kw = False
                if eventos.key == pygame.K_LCTRL:
                    self.ctrl = False
                # INTERAÇÕES DO USUÁRIO
                if self.player.modo == "normal":
                    if eventos.key == pygame.K_a:
                        self.player.btn1 = 1
                    if eventos.key == pygame.K_s:
                        self.player.btn2 = 1
                    if eventos.key == pygame.K_j:
                        self.player.btn3 = 1
                    if eventos.key == pygame.K_k:
                        self.player.btn4 = 1
                elif self.player.modo == "palhetar":
                    if eventos.key == pygame.K_F1:
                        self.player.f1 = False
                    if eventos.key == pygame.K_F2:
                        self.player.f2 = False
                    if eventos.key == pygame.K_F3:
                        self.player.f3 = False
                    if eventos.key == pygame.K_F4:
                        self.player.f4 = False
                    if eventos.key == pygame.K_UP:
                        self.player.cima = False
                    if eventos.key == pygame.K_DOWN:
                        self.player.baixo = False
