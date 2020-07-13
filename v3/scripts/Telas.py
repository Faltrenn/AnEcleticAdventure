from v3.scripts import Recursos
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
        self.comando = [self.comandos]

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
        self.comando = [self.comandos]

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
        self.comando = [self.comandos] # Não Entendi (?)

    def rodar(self, tela):
        tela.janela.blit(self.imagens.back_menu2, self.imagens.back_menu2.get_rect())
        self.botoes.rodar(tela)

    def comandos(self, e, mudar_tela, tela, main):
        self.botoes.comandos(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if self.botoes.selec <= len(self.botoes.botoes) - 2:
                    main.telas["musicas"].definir_musicas(self.infos[self.botoes.selec][0])
                    mudar_tela.trocar_tela(self.nome, "musicas")
                else:
                    mudar_tela.trocar_tela(self.nome, "modos")
                    main.telas[self.nome] = MenuHistoria(self.imagens)


class MenuOnline:
    def __init__(self, imagens):
        self.nome = "online"
        self.aqui = False
        self.imagens = imagens
        self.infos = [["Voltar", (255, 255, 255), (180, 600)]]
        self.botoes = Recursos.Botoes(self.infos)
        self.comando = [self.comandos]

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
        self.comando = [self.comandos]

    def rodar(self, tela):
        tela.janela.blit(self.imagens.back_menu_wip, self.imagens.back_menu_wip.get_rect())
        self.botoes.rodar(tela)

    def comandos(self, e, mudar_tela, tela, main):
        self.botoes.comandos(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if self.botoes.selec == 0:
                    mudar_tela.trocar_tela(self.nome, "modos")
                    main.telas[self.nome] = MenuExtras(self.imagens)


class MenuMusicas:
    def __init__(self, imagens):
        self.nome = "musicas"
        self.aqui = False
        self.imagens = imagens
        self.personagem = ""
        self.musicas = {"Personagem 1": [["Musica1 do P1", False], ["Musica2 do P1", False], ["Musica3 do P1", False]],
                        "Personagem 2": [["Musica1 do P2", False], ["Musica2 do P2", False], ["Musica3 do P2", False]],
                        "Personagem 3": [["Musica1 do P3", False], ["Musica2 do P3", False], ["Musica3 do P3", False]]}
        self.comando = [self.comandos]
        self.infos = []
        self.botoes = None

    def rodar(self, tela):
        tela.janela.blit(self.imagens.back_menu2, self.imagens.back_menu2.get_rect())
        if self.botoes is not None:
            self.botoes.rodar(tela)

    def comandos(self, e, mudar_tela, tela, main):
        self.botoes.comandos(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if self.botoes.selec <= len(self.botoes.botoes) - 2:
                    main.telas["jogo"].tocar_musica(self.musicas[self.botoes.selec][0], tela)
                    mudar_tela.trocar_tela(self.nome, "jogo")

    def definir_musicas(self, personagem):
        self.musicas = self.musicas[personagem]
        for c, musica in enumerate(self.musicas):
            self.infos.append([musica[0], (0, 0, 0), (180, 80 + (100 * c))])
        self.infos.append(["Voltar", (255, 255, 255), (180, 600)])
        self.botoes = Recursos.Botoes(self.infos)


class Jogo:
    def __init__(self, imagens):
        self.nome = "jogo"
        self.aqui = False
        self.imagens = imagens
        self.musica_atual = ""
        self.arquivo_musica = None
        self.tocou = False
        self.comando = [self.comandos]
        self.notas_provisorias = []
        self.notas_na_esteira = []

    def rodar(self, tela):
        tela.janela.blit(self.imagens.back_menu2, self.imagens.back_menu2.get_rect())
        if self.arquivo_musica is not None and not self.tocou:
            self.arquivo_musica.play()
            self.tocou = True

    def comandos(self, e, mudar_tela, tela, main):
        pass

    def tocar_musica(self, musica, tela):
        self.tocou = False
        print(musica)
        self.arquivo_musica = pygame.mixer.Sound("../src/musicas/" + musica + ".ogg")
        self.arquivo_musica.set_volume(tela.volume)
        self.musica_atual = musica
        arquivo = open("../src/musicas/" + musica + ".txt", "r")
        for linha in arquivo:
            for caractere in linha:
                if caractere.isdigit() and caractere != "0":
                    self.notas_provisorias.append(Recursos.Notas(int(caractere), float(linha[9:])))


