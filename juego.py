import pygame
import random

ANCHO=800
ALTO=400
VERDE=[0,255,0]
ROJO=[255,0,0]
BLANCO=[255,255,255]
NEGRO=[0,0,0]

backgroundPosX=0
backgroundPosXSecond=0
velX = 10

def Corte(archivo,an_i,al_i):
    imagen=pygame.image.load(archivo)
    info= imagen.get_rect()
    ian=info[2]
    ial=info[3]
    an_corte= int (ian/an_i )
    al_corte= int (ial/al_i )
    m=[]
    for col in range(al_i):
        l=[]
        for i in range(an_i):
            cuadro = imagen.subsurface(an_corte*i, col * al_corte , an_corte,al_corte)
            l.append(cuadro)
        m.append(l)
    return m, an_corte, al_corte

    
def renderLetters(text="",posx=250,posy=250,size=32,color=BLANCO):
    fuente=pygame.font.Font(None, size)
    texto= fuente.render(text, True, color)
    pantalla.blit(texto,[posx,posy])
    pygame.display.flip()

def showInfinityBackground():
    global backgroundPosX
    fondo=pygame.image.load('background.png')
    if backgroundPosX < ANCHO:
        backgroundPosX=backgroundPosX+velX
        pantalla.blit(pygame.transform.scale(fondo, (ANCHO, ALTO)), (backgroundPosX, 0))
        pantalla.blit(pygame.transform.scale(fondo, (ANCHO, ALTO)), (backgroundPosX-ANCHO, 0))
        pygame.display.flip()
    else:
        backgroundPosX = 0



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    
    reloj=pygame.time.Clock()

    fin=False
    while not fin:

        showInfinityBackground()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        reloj.tick(20)

