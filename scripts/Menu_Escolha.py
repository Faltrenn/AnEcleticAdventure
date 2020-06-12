import pygame

class Menu_Escolha:
    def __init__(self, tela):
        self.menu_escolha = False
        self.tela = tela
        self.w = False
        self.ctrl = False

    def render(self, imagens):
        self.tela.janela.blit(imagens.menu2_background, imagens.menu2_background.get_rect())

    def tick(self):
        if self.w and self.ctrl:
            pygame.quit()
            self.tela.rodando = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                self.tela.rodando = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LCTRL:
                    self.ctrl = True
                if e.key == pygame.K_W:
                    self.w = True

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LCTRL:
                    self.ctrl = False
                if e.key == pygame.K_W:
                    self.w = False
                    
