import pygame
from scripts import Player, Notas
import os

pygame.init()

class Tela:

    def __init__(self):
        self.janela = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        self.rodando = True
        self.ctrl = False
        self.kw = False
        self.fps = 0
        self.antes = 0
        self.player = Player.Player()

        self.tocando = False

        self.m = pygame.mixer.Sound("naruto1.ogg")

        self.antes = pygame.time.get_ticks()
        self.segundos = 0
        self.esteira = list()
        self.notas = list()
        self.arquivo = open("naruto1.txt", "r")
        for linha in self.arquivo:
            for c in range(0, len(linha)):
                if c < 9:
                    if linha[c].isdigit() and linha[c] != "0":
                        self.notas.append(Notas.Nota(int(linha[c]), float(linha[9:]) - 4))
        self.arquivo.close()

    def spawn(self):

        if pygame.time.get_ticks() - self.antes >= 100:
            self.segundos += (pygame.time.get_ticks() - self.antes) / 1000
            self.segundos = float("%.1f" % self.segundos)
            print(self.segundos)

            self.antes = pygame.time.get_ticks()

        for nota in self.notas:
            if nota.tempo == self.segundos:
                self.esteira.append(nota)
                self.notas.remove(nota)

        for nota in self.esteira:
            nota.render(self.janela)
            nota.tick(self.esteira, self.player)


    def render(self):
        self.fps = self.fps + 1
        if pygame.time.get_ticks() - self.antes >= 1000:
            self.antes = pygame.time.get_ticks()

            self.fps = 0
        self.janela.fill((255, 255, 255))

        self.player.render(self.janela)
        self.player.tick()

        self.spawn()

        self.musica()



        self.player.btn1 = self.player.btn2 = self.player.btn3 = self.player.btn4 = 1

        pygame.display.update()

    def musica(self):
        if not self.tocando:
            self.m.play()
            self.tocando = True

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

