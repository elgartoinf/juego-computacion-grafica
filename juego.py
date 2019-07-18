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


class Bloque (pygame.sprite.Sprite):
    def __init__(self, p, dims):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dims)
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]

class Jugador (pygame.sprite.Sprite):
    def __init__(self, p):
        pygame.sprite.Sprite.__init__(self)
        self.m = corte('personaje.png', 8,2)
        self.image = self.m[0][0][0]
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely = 0
        self.vidas=3
        self.siguiente = "d"
        self.sig = 0
        self.plataformas=None
        
    def gravedad(self, cte=0.5):
        if self.vely == 0:
            self.vely = 1
        else:
            self.vely += cte

    def update(self):

        if self.siguiente == "d":
            self.image = self.m[0][0][0+self.sig]
        if self.siguiente == "i":
            self.image = self.m[0][1][0+self.sig]
        if self.siguiente == "a":
            self.image = self.m[0][0][0+self.sig]
        if self.siguiente == "b":
            self.image = self.m[0][0][0+self.sig]


        self.sig = self.sig + 1
        if self.sig == 5:
            self.sig = 0


        if self.velx != 0:
            if self.rect.x <= (ANCHO-200) and self.rect.x >= 0:
                print(self.velx)
                self.rect.x += self.velx
            else:
                if self.rect.x >= 0:
                    self.rect.x -= 50
                else:
                    self.rect.x += 50
        



        self.rect.y += self.vely
        

        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        for p in ls_col:
            if self.rect.top < p.rect.bottom and self.vely < 0:
                self.rect.top = p.rect.bottom + 10
                self.vely = 0
            if self.rect.bottom > p.rect.top and self.vely > 0:
                self.rect.bottom = p.rect.top + 10
                self.vely = 0

        if self.rect.bottom > ALTO:
            self.rect.bottom=ALTO
            self.vely=0

        self.gravedad()



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    jugadores = pygame.sprite.Group()

    j=Jugador([0,ALTO-120])
    jugadores.add(j)    


    plataformas= pygame.sprite.Group()

    p=Bloque([150,100],[120,20])
    plataformas.add(p)

    p=Bloque([1300,200],[120,20])
    plataformas.add(p)

    j.plataformas=plataformas

    reloj=pygame.time.Clock()
    fin=False
    cont = 0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.siguiente = "d"
                    j.velx=10
                    j.vely=0
                if event.key == pygame.K_LEFT:
                    j.siguiente = "i"
                    j.velx= -10
                    j.vely=0
                if event.key == pygame.K_SPACE:
                    j.vely= -10
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

        if j.rect.x <= (ANCHO-200) and j.rect.x >= 0:
            for p in plataformas:
                p.rect.x+=j.velx
                print(p.rect.x,j.velx)

        velX = (j.velx/4)
        if (cont % 4) == 0:
            jugadores.update()
        showInfinityBackground()
        jugadores.draw(pantalla)
        plataformas.draw(pantalla)
        pygame.display.flip()

        cont+=1
        if cont == 60:
            cont = 0
