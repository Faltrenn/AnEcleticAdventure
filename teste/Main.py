from teste import Mapa1, Mapa2, MudarMapa
from time import sleep

mapa1 = Mapa1.Mapa1()
mapa2 = Mapa2.Mapa2()
mapas = {"mapa1": mapa1,
         "mapa2": mapa2}
mudar_mapa = MudarMapa.MudarMapa(mapas)

mudar_mapa.trocarMapa("mapa1", "mapa2")


def render():
    if mapa1.nesse_mapa:
        mapa1.render()
    if mapa2.nesse_mapa:
        mapa2.render()


while True:
    render()

    sleep(0.5)