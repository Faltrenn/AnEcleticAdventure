class MudarMapa:
    def __init__(self, mapas):
        self.mapas = mapas

    def trocarMapa(self, saindo_de, indo_para):
        self.mapas[saindo_de].nesse_mapa = False
        self.mapas[indo_para].nesse_mapa = True