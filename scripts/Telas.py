from scripts import Recursos
import pygame


class MudarTela:
    def __init__(self, telas):
        self.telas = telas

    def trocar_tela(self, tela_atual, tela_alvo):
        self.telas[tela_atual].aqui = False
        self.telas[tela_alvo].aqui = True


class MenuPrincipal:
    def __init__(self, imagens):
        self.nome = "principal"
        self.aqui = True
        self.imagens = imagens
        self.infos = [["Jogar", (0, 0, 0), (450, 400)], ["Sair", (255, 255, 255), (750, 400)]]
        self.botoes = Recursos.Botoes(self.infos)
        self.comandos = [self.comandos]

    def rodar(self, tela):
        tela.janela.blit(self.imagens.back_menu_principal, self.imagens.back_menu_principal.get_rect())
        self.botoes.rodar(tela)

    def comandos(self, e, mudar_tela, tela, main):
        self.botoes.comandos(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if self.botoes.selec == 0:
                    mudar_tela.trocar_tela(self.nome, "modos")
                else:
                    pygame.quit()
                    tela.rodando = False


class MenuModos:
    def __init__(self, imagens):
        self.nome = "modos"
        self.aqui = False
        self.imagens = imagens
        self.infos = [["História", (0, 0, 0), (180, 80)],
                      ["Online", (0, 0, 0), (180, 180)],
                      ["Musicas Extras", (0, 0, 0), (180, 280)],
                      ["Voltar", (255, 255, 255), (180, 600)]]
        self.botoes = Recursos.Botoes(self.infos)
        self.comandos = [self.comandos]

    def rodar(self, tela):
        tela.janela.blit(self.imagens.back_menu2, self.imagens.back_menu2.get_rect())
        self.botoes.rodar(tela)

    def comandos(self, e, mudar_tela, tela, main):
        self.botoes.comandos(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if self.botoes.selec == 0:
                    mudar_tela.trocar_tela(self.nome, "historia")
                elif self.botoes.selec == 1:
                    mudar_tela.trocar_tela(self.nome, "online")
                elif self.botoes.selec == 2:
                    mudar_tela.trocar_tela(self.nome, "extras")
                elif self.botoes.selec == 3:
                    mudar_tela.trocar_tela(self.nome, "principal")
                    main.telas[self.nome] = MenuModos(self.imagens)

class MenuHistoria:
    def __init__(self, imagens):
        self.nome = "historia"
        self.aqui = False
        self.imagens = imagens
        self.infos = [["Personagem 1", (0, 0, 0), (180, 80)],
                      ["Personagem 2", (0, 0, 0), (180, 180)],
                      ["Personagem 3", (0, 0, 0), (180, 280)],
                      ["Voltar", (255, 255, 255), (180, 600)]]
        self.botoes = Recursos.Botoes(self.infos)
        self.comandos = [self.comandos] # Não Entendi (?)

    def rodar(self, tela):
        tela.janela.blit(self.imagens.back_menu2, self.imagens.back_menu2.get_rect())
        self.botoes.rodar(tela)

    def comandos(self, e, mudar_tela, tela, main):
        self.botoes.comandos(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if self.botoes.selec == 0:
                    mudar_tela.trocar_tela(self.nome, "personagem1")
                elif self.botoes.selec == 1:
                    mudar_tela.trocar_tela(self.nome, "personagem2")
                elif self.botoes.selec == 2:
                    mudar_tela.trocar_tela(self.nome, "personagem3")
                elif self.botoes.selec == 3:
                    mudar_tela.trocar_tela(self.nome, "modos")
                    main.telas[self.nome] = MenuHistoria(self.imagens)

class MenuOnline:
    def __init__(self, imagens):
        self.nome = "online"
        self.aqui = False
        self.imagens = imagens
        self.infos = [["Voltar", (255, 255, 255), (180, 600)]]
        self.botoes = Recursos.Botoes(self.infos)
        self.comandos = [self.comandos]

    def rodar(self, tela):
        tela.janela.blit(self.imagens.back_menu_wip, self.imagens.back_menu_wip.get_rect())
        self.botoes.rodar(tela)

    def comandos(self, e, mudar_tela, tela, main):
        self.botoes.comandos(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if self.botoes.selec == 0:
                    mudar_tela.trocar_tela(self.nome, "modos")
                    main.telas[self.nome] = MenuOnline(self.imagens)

class MenuExtras:
    def __init__(self, imagens):
        self.nome = "extras"
        self.aqui = False
        self.imagens = imagens
        self.infos = [["Voltar", (255, 255, 255), (180, 600)]]
        self.botoes = Recursos.Botoes(self.infos)
        self.comandos = [self.comandos]

    def rodar(self, tela):
        tela.janela.blit(self.imagens.back_menu_wip, self.imagens.back_menu_wip.get_rect())
        self.botoes.rodar(tela)

    def comandos(self, e, mudar_tela, tela, main):
        self.botoes.comandos(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if self.botoes.selec == 0:
                    mudar_tela.trocar_tela(self.nome, "modos")
                    main.telas[self.nome] = MenuOnline(self.imagens)



