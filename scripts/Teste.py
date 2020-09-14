import pygame

tela = pygame.display.set_mode((1280, 720))

rodando = True

imagem = pygame.image.load("../src/imagens/blank2fade2.jpg").convert()
imagem1_posy = 400
imagem2_posy = 100

while rodando:

    if imagem1_posy < imagem2_posy:
        imagem1_posy += 2
        imagem2_posy = imagem1_posy + 300
    else:
        imagem2_posy += 2
        imagem1_posy = imagem2_posy + 300

    if imagem1_posy >= 700:
        imagem1_posy = 100
    if imagem2_posy >= 700:
        imagem2_posy = 100

    tela.fill((0, 0, 0))
    tela.blit(imagem, (500, imagem1_posy, 203, 300))
    tela.blit(imagem, (500, imagem2_posy, 203, 300))
    pygame.display.update()

    pygame.time.Clock().tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            rodando = False
            pygame.quit()
