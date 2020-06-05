import pygame
from scripts import Notas, Player

pygame.init()


class Tela:
    def __init__(self):
        self.janela = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        self.notas = []
        self.rodando = True
        self.ctrl = False
        self.kw = False

        self.player = Player.Player()

    def render(self, janela, objTela):
        self.janela.fill((255, 255, 255))
        for nota in self.notas:
            nota.render(janela)
            nota.tick(objTela)

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
            elif eventos.type == pygame.KEYUP:
                if eventos.key == pygame.K_w:
                    self.kw = False
                if eventos.key == pygame.K_LCTRL:
                    self.ctrl = False
                # INTERAÇÕES DO USUÁRIO
                if eventos.key == pygame.K_a:
                    self.player.btn1 = 1
    #TESTE 1 12 3