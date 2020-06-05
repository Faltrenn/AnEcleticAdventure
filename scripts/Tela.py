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

    def render(self, janela, objTela):
        self.fps = self.fps + 1
        if pygame.time.get_ticks() - self.antes >= 1000:
            self.antes = pygame.time.get_ticks()
            print(self.fps)
            self.fps = 0
        self.janela.fill((255, 255, 255))
        for nota in self.notas:
            nota.render(janela)
            nota.tick(objTela, self.player)

        self.player.render(janela)

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
                if eventos.key == pygame.K_a:
                    self.player.btn1 = 0
                if eventos.key == pygame.K_s:
                    self.player.btn2 = 0
                if eventos.key == pygame.K_j:
                    self.player.btn3 = 0
                if eventos.key == pygame.K_k:
                    self.player.btn4 = 0
            elif eventos.type == pygame.KEYUP:
                if eventos.key == pygame.K_w:
                    self.kw = False
                if eventos.key == pygame.K_LCTRL:
                    self.ctrl = False
                # INTERAÇÕES DO USUÁRIO
                if eventos.key == pygame.K_a:
                    self.player.btn1 = 1
                if eventos.key == pygame.K_s:
                    self.player.btn2 = 1
                if eventos.key == pygame.K_j:
                    self.player.btn3 = 1
                if eventos.key == pygame.K_k:
                    self.player.btn4 = 1