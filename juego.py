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
velX = -10

def corte(archivo,an_i,al_i):
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
    print(backgroundPosX)
    if backgroundPosX >= 0:
        if backgroundPosX < ANCHO:
            backgroundPosX=backgroundPosX+velX
            pantalla.blit(pygame.transform.scale(fondo, (ANCHO, ALTO)), (backgroundPosX, 0))
            pantalla.blit(pygame.transform.scale(fondo, (ANCHO, ALTO)), (backgroundPosX-ANCHO, 0))
        else:
            backgroundPosX = 0
    else:
        if (-backgroundPosX) > ANCHO:
            backgroundPosX = -1
        backgroundPosX=backgroundPosX+velX
        pantalla.blit(pygame.transform.scale(fondo, (ANCHO, ALTO)), (backgroundPosX, 0))
        pantalla.blit(pygame.transform.scale(fondo, (ANCHO, ALTO)), (backgroundPosX+ANCHO, 0))


class Jugador (pygame.sprite.Sprite):
    def __init__(self, p):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([40,50])
        #self.image.fill(BLANCO)
        self.m = corte('personaje.png', 5,4)
        self.image = self.m[0][0][0]
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely = 0
        self.vidas=3
        self.siguiente = "d"
        self.sig = 0
        

    def update(self):

        if self.siguiente == "d":
            self.image = self.m[0][0][0+self.sig]
        if self.siguiente == "i":
            self.image = self.m[0][0][0+self.sig]
        if self.siguiente == "a":
            self.image = self.m[0][0][0+self.sig]
        if self.siguiente == "b":
            self.image = self.m[0][0][0+self.sig]


        self.sig = self.sig + 1
        if self.sig == 2:
            self.sig = 0


        if self.velx != 0:
            self.rect.x += self.velx
        if self.vely != 0:
            self.rect.y += self.vely



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    jugadores = pygame.sprite.Group()
    j=Jugador([100,100])
    jugadores.add(j)    
    #reloj=pygame.time.Clock()

    fin=False
    while not fin:
        showInfinityBackground()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.siguiente = "d"
                    j.velx=5
                    j.vely=0
                if event.key == pygame.K_LEFT:
                    j.siguiente = "i"
                    j.velx= -5
                    j.vely=0
                if event.key == pygame.K_UP:
                    j.siguiente = "a"
                    j.vely=-5
                    j.velx=0
                if event.key == pygame.K_DOWN:
                    j.siguiente = "b"
                    j.vely=5
                    j.velx=0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j.velx=0
                    j.vely=0
                if event.key == pygame.K_LEFT:
                    j.velx=0
                    j.vely=0
                if event.key == pygame.K_UP:
                    j.velx=0
                    j.vely=0
                if event.key == pygame.K_DOWN:
                    j.velx=0
                    j.vely=0


            velX = j.velx
            #jugadores.update()
            jugadores.draw(pantalla)
        
        pygame.display.flip()
        #reloj.tick(20)
