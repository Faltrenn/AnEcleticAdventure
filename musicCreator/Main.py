import pygame
from musicCreator import Logica

pygame.mixer.init()
pygame.init()

tela = Logica.Tela()


relogio = pygame.time.Clock()
antes = pygame.time.get_ticks()
Antes = 0

txt = open('txt.txt', 'w')

pygame.mixer.music.load('../scripts/musica.ogg')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1.0)

while pygame.mixer.music.get_busy():  # MAIN LOOP

    if pygame.display.get_surface() is not None and pygame.get_init():
        tela.trigger()

        try:
            tela.render()

        except:
            print(True)
            break


    if pygame.time.get_ticks() - Antes >= 100:
        segundos = (pygame.time.get_ticks() - antes) / 1000
        segundos = "%.1f" % segundos

        txt.write("("+str(tela.btn1)+","+str(tela.btn2)+","+str(tela.btn3)+","+str(tela.btn4)+")"+str(segundos)+"\n")
        print("(",tela.btn1, ",", tela.btn2, ",", tela.btn3, ",", tela.btn4, ",", segundos, ")")

        Antes = pygame.time.get_ticks()


    relogio.tick(60)


