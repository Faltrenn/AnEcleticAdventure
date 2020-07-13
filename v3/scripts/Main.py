from v3.scripts import Player, Recursos, Telas
import pygame


pygame.init()


class Main:
    def __init__(self):
        # Recursos
        self.tela = Recursos.Tela()
        self.fontes = Recursos.Fontes()
        self.imagens = Recursos.Imagens()
        self.relogio = pygame.time.Clock()

        self.antes = self.agora = self.fps = 0

        self.player = Player.Player()

        # Menus
        self.telas = {"principal": Telas.MenuPrincipal(self.imagens),  # Principal -> História -> P1|P2|P3 -> Musicas
                      "modos": Telas.MenuModos(self.imagens),  # -> Online
                      "historia": Telas.MenuHistoria(self.imagens),  # -> Extras -> Musicas
                      "online": Telas.MenuOnline(self.imagens),
                      "extras": Telas.MenuExtras(self.imagens),
                      "musicas": Telas.MenuMusicas(self.imagens),
                      "jogo": Telas.Jogo(self.imagens)}
        self.mudar_tela = Telas.MudarTela(self.telas)

    def loop(self): #Não Entendi (?)
        while self.tela.rodando:
            self.fps += 1
            self.agora = pygame.time.get_ticks()
            if self.agora - self.antes >= 1000:
                print(f"FPS: {self.fps}")
                self.fps = 0
                self.antes = self.agora
            self.tela.janela.fill((0, 0, 0))
            for nome, menu in self.telas.items():
                if menu.aqui:
                    self.tela.tick(menu.comando, self.mudar_tela, self)
                    if pygame.display.get_surface() is not None:
                        menu.rodar(self.tela)
                        pygame.display.update()

            self.relogio.tick(60)


main = Main()
main.loop()
