class Mudar_Menu:
    def __init__(self, telas):
        self.telas = telas

    def mudar_tela(self, tela_atual, proxima_tela):
        self.telas[tela_atual].aqui = False
        self.telas[proxima_tela].aqui = True
