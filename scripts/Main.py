from scripts import Recursos, Telas
import pygame


pygame.init()


class Main:
    def __init__(self):
        # Recursos
        self.tela = Recursos.Tela()
        self.fontes = Recursos.Fontes()
        self.imagens = Recursos.Imagens()
        self.relogio = pygame.time.Clock()

        # Menus
        self.telas = {"principal": Telas.MenuPrincipal(self.imagens),
                      "modos": Telas.MenuModos(self.imagens)}
        self.mudar_tela = Telas.MudarTela(self.telas)

    def loop(self):
        while self.tela.rodando:
            self.tela.janela.fill((0, 0, 0))
            for nome, menu in self.telas.items():
                if menu.aqui:
                    self.tela.tick(menu.comandos, self.mudar_tela, self)
                    if pygame.display.get_surface() is not None:
                        menu.rodar(self.tela)
                        pygame.display.update()

        self.relogio.tick(60)


main = Main()
main.loop()
