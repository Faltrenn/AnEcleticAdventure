class Botoes:
    def __init__(self, fontes, textos, cores, posicoes):
        self.fontes = fontes
        self.botoes = list()
        self.textos = textos
        self.cores = cores
        self.posicoes = posicoes

    def render(self, selecionado, tela):
        self.botoes = []
        for c in range(0, len(self.textos)):
            self.botoes.append([self.fontes.fonte.render(self.textos[c], True, self.cores[c]), self.posicoes[c]])
        self.botoes[selecionado][0] = self.fontes.fonte_selecionado.render(self.textos[selecionado], True, self.cores[selecionado])
        for botao in self.botoes:
            tela.janela.blit(botao[0], botao[1])
