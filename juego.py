import pygame
import random
from pygame.math import Vector2
import time


ANCHO=800
ALTO=400
VERDE=[0,255,0]
ROJO=[255,0,0]
BLANCO=[255,255,255]
NEGRO=[0,0,0]
AMARILLO=[255,255,0]

backgroundPosX=0
backgroundPosXSecond=0
velX = -10

def eventos(event):
    if event.type == pygame.QUIT:
        fin=True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            j.siguiente = "d"
            if j.velocidad:
                j.velx= 20
            else:
                j.velx=10
            j.vely=0
        if event.key == pygame.K_LEFT:
            j.siguiente = "i"
            if j.velocidad:
                j.velx= -20
            else:
                j.velx=-10
            j.vely=0
        if event.key == pygame.K_UP:
            j.vely = -10
        if event.key == pygame.K_SPACE:
            b=Bala([j.rect.x, j.rect.y])
            if j.siguiente == "i":
                b.velx = -4
            else:
                b.velx = 4
            j.bum.play()
            balas.add(b)
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

def estanCerca(uno, dos, radio=400):
    if uno != dos:
        distancia = Vector2(uno.rect.center).distance_to(dos.rect.center)
        return distancia < radio
    else:
        return False

def mostrarMensajes():
    global mensaje
    if mensaje != "":
        texto=pygame.font.Font(None, 25).render(mensaje, True, VERDE)
        pantalla.blit(texto,[(ANCHO/2-100),(ALTO/2)])
        pygame.display.flip()
        time.sleep(2)
        mensaje = ""

    #vidas
    vidasTexto= "vidas restantes: {}".format(j.vidas)
    texto=pygame.font.Font(None, 25).render(vidasTexto, True, AMARILLO)
    pantalla.blit(texto,[10,20])

def colisionBalasEnemigos():
    global j
    global plataformas
    global fin_juego
    global mensaje
    global boss_murio

    for r in enemigos1:
        ls=pygame.sprite.spritecollide(r,jugadores,True)
        if len(ls) != 0:
            for jjugador in ls:
                vidas = j.vidas - 1
                if vidas > 0:
                    j=Jugador([0,ALTO-120])
                    j.vidas = vidas
                    j.plataformas = plataformas
                    jugadores.add(j)
                    mensaje = "no detendras mi furia!!!!"
                else:
                    mensaje = "Morire cuando muera!!! ...... mori T_T"
                    fin_juego=True

    for r in enemigos2:
        ls=pygame.sprite.spritecollide(r,jugadores,True)
        if len(ls) != 0:
            for jjugador in ls:
                vidas = j.vidas - 1
                if vidas > 0:
                    j=Jugador([0,ALTO-120])
                    j.vidas = vidas
                    j.plataformas = plataformas
                    jugadores.add(j)
                    mensaje = "no detendras mi furia!!!!"
                else:
                    mensaje = "Morire cuando muera!!! ...... mori T_T"
                    fin_juego=True

    for r in enemigos3:
        ls=pygame.sprite.spritecollide(r,jugadores,True)
        if len(ls) != 0:
            for jjugador in ls:
                vidas = j.vidas - 1
                if vidas > 0:
                    j=Jugador([0,ALTO-120])
                    j.vidas = vidas
                    j.plataformas = plataformas
                    jugadores.add(j)
                    mensaje = "no detendras mi furia!!!!"
                else:
                    mensaje = "Morire cuando muera!!! ...... mori T_T"
                    fin_juego=True

    for m in modificadores1:
        ls=pygame.sprite.spritecollide(m,jugadores,False)
        for e in ls:
            modificadores1.remove(m)
            j.poder = True

    for m in modificadores2:
        ls=pygame.sprite.spritecollide(m,jugadores,False)
        for e in ls:
            modificadores2.remove(m)
            j.velocidad = True

    for b in balas:
        ls=pygame.sprite.spritecollide(b,enemigos1,True)
        for e in ls:
            balas.remove(b)
            enemigo1.vidas-=1
            if enemigo1.vidas == 0:
                enemigos1.remove(enemigo1)
                mensaje = "Mis hermanos te venceran kathmandu"
        if b.rect.x < -20:
            balas.remove(b)

    for b in balas:
        ls=pygame.sprite.spritecollide(b,enemigos2,True)
        for e in ls:
            balas.remove(b)
            enemigo2.vidas-=1
            if enemigo2.vidas == 0:
                enemigos2.remove(enemigo2)
                mensaje = "moriras en de hambre devilucho!!"
        if b.rect.x < -20:
            balas.remove(b)


    for b in balas:
        ls=pygame.sprite.spritecollide(b,enemigos3,True)
        for e in ls:
            balas.remove(b)
            enemigo3.vidas-=1
            if enemigo3.vidas == 0:
                enemigos3.remove(enemigo3)
                mensaje = "por las barbas de odin!!!"
        if b.rect.x < -20:
            balas.remove(b)


    for b in balas:
        if estanCerca(boss,j,600):
            ls=pygame.sprite.spritecollide(b,bosses,False)
            for e in ls:
                balas.remove(b)
                boss.vidas-=1
                if boss.vidas == 0:
                    bosses.remove(boss)
                    mensaje = "por las barbas de odin mori!!!!"
                    boss_murio = True
                    fin_juego = True
            if b.rect.x < -20:
                balas.remove(b)


    for b in balasEnemigo1:
        ls=pygame.sprite.spritecollide(b,jugadores,True)
        if len(ls) != 0:
            for jjugador in ls:
                vidas = j.vidas - 1
                balasEnemigo1.remove(b)
                if vidas > 0:
                    j=Jugador([0,ALTO-120])
                    j.vidas = vidas
                    j.plataformas = plataformas
                    jugadores.add(j)
                    mensaje = "no detendras mi furia!!!!"
                else:
                    mensaje = "Morire cuando muera!!! ...... mori T_T"
                    fin_juego=True


    for b in bosses:
        ls=pygame.sprite.spritecollide(b,jugadores,True)
        if len(ls) != 0:
            for jjugador in ls:
                vidas = j.vidas - 1
                if vidas > 0:
                    j=Jugador([0,ALTO-120])
                    j.vidas = vidas
                    j.plataformas = plataformas
                    jugadores.add(j)
                    mensaje = "no detendras mi furia!!!!"
                else:
                    mensaje = "Morire cuando muera!!! ...... mori T_T"
                    fin_juego=True

def corte(archivo,an_i,al_i,scale=1):
    imagen=pygame.transform.scale(pygame.image.load(archivo), (pygame.image.load(archivo).get_width()*scale, pygame.image.load(archivo).get_height()*scale))
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

class Enemigo1(pygame.sprite.Sprite):
    def __init__(self, p, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.uno = corte('enemigo1_0.png', 6,1)
        self.dos = corte('enemigo1_1.png', 6,1)
        self.image = self.uno[0][0][0]
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.sig = 0
        self.vely = 4
        self.siguiente = "p"
        self.plataformas=None
        self.vidas = 3

    def update(self):
        if self.siguiente == "p":
            self.image = self.uno[0][0][0+self.sig]
        else:
            self.image = self.dos[0][0][0+self.sig]

        self.sig = self.sig + 1
        if self.sig == 5:
            self.sig = 0

        


        ########## colision con  la plataforma ######
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        if len(ls_col) == 0:
            if self.rect.y > (ALTO-self.rect.height):
                self.vely=-5
            if self.rect.y < 0:
                self.vely=5

            self.rect.y += self.vely
        else:
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

class Enemigo2(pygame.sprite.Sprite):
    def __init__(self, p, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.uno = corte('enemigo2_0.png', 6,1)
        self.dos = corte('enemigo2_1.png', 6,1)
        self.image = self.uno[0][0][0]
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.sig = 0
        self.vely = 4
        self.velx = 0
        self.siguiente = "p"
        self.plataformas=None
        self.vidas = 3

    def update(self):
        if self.siguiente == "p":
            self.image = self.uno[0][0][0+self.sig]
        else:
            self.image = self.dos[0][0][0+self.sig]

        self.sig = self.sig + 1
        if self.sig == 5:
            self.sig = 0

        


        ########## colision con  la plataforma ######
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        if len(ls_col) == 0:
            if self.rect.y > (ALTO-self.rect.height):
                self.vely=-5
            if self.rect.y < 0:
                self.vely=5

            self.rect.y += self.vely

            self.rect.x += self.velx

        else:
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

class Enemigo3(pygame.sprite.Sprite):
    def __init__(self, p, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.uno = corte('enemigo3_0.png', 6,1)
        self.dos = corte('enemigo3_1.png', 6,1)
        self.image = self.uno[0][0][0]
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.sig = 0
        self.vely = 0
        self.velx = 0
        self.siguiente = "p"
        self.plataformas=None
        self.vidas = 3

    def update(self):
        if self.siguiente == "p":
            self.image = self.uno[0][0][0+self.sig]
        else:
            self.image = self.dos[0][0][0+self.sig]

        self.sig = self.sig + 1
        if self.sig == 5:
            self.sig = 0

        


        ########## colision con  la plataforma ######
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        if len(ls_col) == 0:
            self.rect.x += (self.velx * 2)

        else:
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

class Boss(pygame.sprite.Sprite):
    def __init__(self, p, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.uno = corte('boss_1.png', 4,1,3)
        self.dos = corte('boss_0.png', 4,1,3)
        self.image = self.uno[0][0][0]
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.sig = 0
        self.vely = 0
        self.velx = 0
        self.siguiente = "p"
        self.plataformas=None
        self.vidas = 20

    def update(self):
        if self.siguiente == "p":
            self.image = self.uno[0][0][0+self.sig]
        if self.siguiente == "s":
            self.image = self.dos[0][0][0+self.sig]

        self.sig = self.sig + 1
        if self.sig == 4:
            self.sig = 0
        


        ########## colision con  la plataforma ######
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        if len(ls_col) == 0:
            self.rect.x += (self.velx * 2)

        else:
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

class Bala(pygame.sprite.Sprite):
    def __init__(self, p, cl=BLANCO):
        bala=pygame.image.load('bullet.png')
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bala, (40, 40))
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0

    def update(self):
        self.rect.x += self.velx


class Modificador(pygame.sprite.Sprite):
    def __init__(self):
        bala=pygame.image.load('bullet.png')
        pygame.sprite.Sprite.__init__(self)


class Bloque (pygame.sprite.Sprite):
    def __init__(self, p, dims):
        pygame.sprite.Sprite.__init__(self)
        self.dims = dims
        self.image=pygame.Surface(dims)
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]

class VidaBoss(Bloque):
    
    def update(self):
        self.image=pygame.Surface([int(self.dims[0]*(((boss.vidas*100)/20)/100)),self.dims[1]])
        self.image.fill(AMARILLO)
        self.rect=self.image.get_rect()

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
        self.bum=pygame.mixer.Sound('bum.wav')
        self.poder = False
        self.velocidad = False

        
    def gravedad(self, cte=2):
        if self.vely == 0:
            self.vely = 1
        else:
            self.vely += cte

    def update(self):
        global mensaje
        global fin_juego
        
        if not self.poder:
            if self.siguiente == "d":
                self.image = self.m[0][0][0+self.sig]
            if self.siguiente == "i":
                self.image = self.m[0][1][0+self.sig]
            if self.siguiente == "a":
                self.image = self.m[0][0][0+self.sig]
            if self.siguiente == "b":
                self.image = self.m[0][0][0+self.sig]
        else:
            if self.siguiente == "d":
                self.image = pygame.transform.scale(self.m[0][0][0+self.sig], (int(self.m[0][0][0+self.sig].get_width()*0.5), int(self.m[0][0][0+self.sig].get_width()*0.5)))
            if self.siguiente == "i":
                self.image = pygame.transform.scale(self.m[0][1][0+self.sig], (int(self.m[0][1][0+self.sig].get_width()*0.5), int(self.m[0][1][0+self.sig].get_width()*0.5)))
            if self.siguiente == "a":
                self.image = pygame.transform.scale(self.m[0][0][0+self.sig], (int(self.m[0][0][0+self.sig].get_width()*0.5), int(self.m[0][0][0+self.sig].get_width()*0.5)))
            if self.siguiente == "b":
                self.image = pygame.transform.scale(self.m[0][0][0+self.sig], (int(self.m[0][0][0+self.sig].get_width()*0.5), int(self.m[0][0][0+self.sig].get_width()*0.5)))


        self.sig = self.sig + 1
        if self.sig == 5:
            self.sig = 0


        if self.velx != 0:
            if self.rect.x <= (ANCHO-200) and self.rect.x >= 0:
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


        if self.poder and self.vely != 0:
            if (self.rect.bottom - 60) < ALTO:
                self.rect.y += self.vely
            else:
                self.vely = 0
        else:
            if self.rect.bottom < ALTO:
                self.rect.y += self.vely
            else:
                self.vely = 0 



        self.gravedad()


        if self.rect.y > ALTO:
            self.vidas = 0
            mensaje = "Me hundi!!!!! y mori!!"
            fin_juego=True



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    reloj = pygame.time.Clock()

    contadorPder1 = 0
    contadorPder2 = 0
    pos_y1=300
    vel_y=-5

    fin = False
    #TODO: cambiar
    fin_mostrar = True
    while not fin and not fin_mostrar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        texto0= pygame.font.Font(None, 32).render('En un principio el Jefe de nivel y el jugador pelearon por comida y honor.', True, ROJO)
        texto= pygame.font.Font(None, 32).render('Jefe de nivel: Te matare devilucho!!!!!!', True, ROJO)
        texto2= pygame.font.Font(None, 32).render('y me comere tus huesos porque no tienes carne flacucha(o)', True, ROJO)
        texto1=pygame.font.Font(None, 32).render('Jugador: Te matare y comere ensalada de frutas', True,BLANCO)
        texto3= pygame.font.Font(None, 32).render('Jefe de nivel: Primero tendras matar a mis compinches Bujajajajaja!!', True, ROJO)
        texto4=pygame.font.Font(None, 32).render('Jugador: este desierto se esta hundiendo!!!', True,BLANCO)


        if pos_y1+250 < 0:
            fin_mostrar=True

        pantalla.fill(NEGRO)
        pantalla.blit(texto,[0,pos_y1])
        pantalla.blit(texto0,[0,pos_y1+50])
        pantalla.blit(texto2,[0,pos_y1+100])
        pantalla.blit(texto1,[0,pos_y1+150])
        pantalla.blit(texto3,[0,pos_y1+200])
        pantalla.blit(texto4,[0,pos_y1+250])
        pygame.display.flip()
        reloj.tick(10)
        pos_y1+=vel_y



    jugadores = pygame.sprite.Group()

    j=Jugador([0,ALTO-120])
    jugadores.add(j)    


    plataformas= pygame.sprite.Group()

    for i in range(0,10):        
        p=Bloque([random.randrange(100, ANCHO*10),random.randrange(100, 300)],[random.randrange(100, 200),20])
        plataformas.add(p)


    balas = pygame.sprite.Group()
    balasEnemigo1 = pygame.sprite.Group()

    j.plataformas=plataformas

    enemigos1 = pygame.sprite.Group()
    enemigo1 = Enemigo1([900,0])
    enemigos1.add(enemigo1)
    enemigo1.plataformas = plataformas


    enemigos2 = pygame.sprite.Group()
    enemigo2 = Enemigo2([1500,0])
    enemigos2.add(enemigo2)
    enemigo2.plataformas = plataformas


    enemigos3 = pygame.sprite.Group()
    enemigo3 = Enemigo3([800,ALTO - 100])
    enemigos3.add(enemigo3)
    enemigo3.plataformas = plataformas


    bosses = pygame.sprite.Group()
    boss = Boss([3700,ALTO-220])
    bosses.add(boss)
    boss.plataformas = plataformas

    vidabosses = pygame.sprite.Group()
    vidaboss = VidaBoss([0,ALTO-10],[ANCHO,10])
    vidabosses.add(vidaboss)


    modificadores1 = pygame.sprite.Group()
    modificador1 = Modificador()
    modificador1.image = pygame.transform.scale(pygame.image.load('poder1.png'), (60, 60))
    modificador1.rect=modificador1.image.get_rect()
    modificador1.rect.x= random.randrange(900, 1200)
    modificador1.rect.y= ALTO - 70
    modificadores1.add(modificador1)


    modificadores2 = pygame.sprite.Group()
    modificador2 = Modificador()
    modificador2.image = pygame.transform.scale(pygame.image.load('poder2.png'), (60, 60))
    modificador2.rect=modificador2.image.get_rect()
    modificador2.rect.x= random.randrange(100, 500)
    modificador2.rect.y= ALTO - 70
    modificadores2.add(modificador2)

    reloj=pygame.time.Clock()
    fin=False
    fin_juego = False
    mensaje_boss = False
    boss_murio = False
    cont = 0

    mensaje = ""

    while not (fin or fin_juego):
        for event in pygame.event.get():
            eventos(event)

        if j.rect.x <= (ANCHO-200) and j.rect.x >= 0:
            for p in plataformas:
                p.rect.x+=-j.velx

            modificador1.rect.x += -j.velx
            modificador2.rect.x += -j.velx

            if not estanCerca(enemigo1,j,600):
                enemigo1.rect.x+=-j.velx
                enemigo1.rect.y = 0

            if not estanCerca(enemigo2,j,600):
                enemigo2.rect.x+=-j.velx
                enemigo2.rect.y = 0

            if not estanCerca(enemigo3,j,600):
                enemigo3.rect.x+=-j.velx
                enemigo3.rect.y = ALTO - 100

            if not estanCerca(boss,j,300):
                boss.rect.x+=-j.velx


            if estanCerca(enemigo1,j) and (cont % 80) == 0:
                if len(enemigos1) != 0:
                    b=Bala([enemigo1.rect.x, enemigo1.rect.y])
                    b.image = pygame.transform.scale(pygame.image.load('bullet_1.png'), (20, 20))
                    if j.rect.x < enemigo1.rect.x:
                        b.velx = -4
                        enemigo1.siguiente = "s"
                    else:
                        b.velx = 4
                        enemigo1.siguiente = "p"
                    balasEnemigo1.add(b)

            if estanCerca(enemigo2,j,600) and (cont % 80) == 0:
                if len(enemigos2) != 0:
                    b=Bala([enemigo2.rect.x, enemigo2.rect.y])
                    b.image = pygame.transform.scale(pygame.image.load('bullet_1.png'), (20, 20))
                    if j.rect.x < enemigo2.rect.x:
                        b.velx = -4
                        enemigo2.siguiente = "p"
                    else:
                        b.velx = 4
                        enemigo2.siguiente = "s"
                    enemigo2.velx = -j.velx
                    balasEnemigo1.add(b)


            if estanCerca(enemigo3,j,600) and (cont % 80) == 0:
                if len(enemigos3) != 0:
                    b=Bala([enemigo3.rect.x, enemigo3.rect.y])
                    b.image = pygame.transform.scale(pygame.image.load('bullet_1.png'), (20, 20))
                    if j.rect.x < enemigo3.rect.x:
                        b.velx = -4
                        enemigo3.siguiente = "p"
                    else:
                        b.velx = 4
                        enemigo3.siguiente = "s"
                    enemigo3.velx = -j.velx
                    balasEnemigo1.add(b)


            if estanCerca(boss,j,300) and (cont % 80) == 0:
                if not mensaje_boss:
                    mensaje = "Moriras devilucho"
                    mensaje_boss = True
                if j.rect.x < boss.rect.x:
                    boss.siguiente = "s"
                    boss.velx = - 7
                else:
                    boss.siguiente = "p"
                    boss.velx = 7
                boss.velx = -j.velx

        colisionBalasEnemigos()


        velX = (j.velx/4)
        if (cont % 4) == 0:
            jugadores.update()

        

        showInfinityBackground()

        balas.update()
        balas.draw(pantalla)

        balasEnemigo1.update()
        balasEnemigo1.draw(pantalla)
        jugadores.draw(pantalla)

        plataformas.draw(pantalla)
        
        if (cont % 6) == 0:
            enemigos1.update()

        enemigos1.draw(pantalla)


        if (cont % 6) == 0:
            enemigos2.update()

        enemigos2.draw(pantalla)


        if (cont % 6) == 0:
            enemigos3.update()

        enemigos3.draw(pantalla)


        if (cont % 6) == 0:
            bosses.update()

        bosses.draw(pantalla)
        
        if mensaje_boss:
            vidaboss.update()
            vidabosses.draw(pantalla)
        

        modificadores1.draw(pantalla)
        modificadores2.draw(pantalla)

        mostrarMensajes()

        pygame.display.flip()

        cont+=1
        if cont == 120:
            cont = 0

        if j.poder:
            contadorPder1+=1

        if contadorPder1 == 1199:
            j.poder = False


        if j.velocidad:
            contadorPder2+=1

        if contadorPder2 == 1199:
            j.velocidad = False

    if boss_murio:
        pantalla.fill(NEGRO)
        texto= pygame.font.Font(None, 50).render('Ganaste!!! has adquirido el maximo de poder!', True, BLANCO)
        pantalla.blit(texto, [10,(ALTO/2-10)])
        pygame.display.flip() 
    else:
        ########### si fin del juego ############ 
        pantalla.fill(NEGRO)
        texto= pygame.font.Font(None, 50).render('Fin de juego', True, BLANCO)
        pantalla.blit(texto, [(ANCHO/2-100),(ALTO/2-10)])
        pygame.display.flip()
    
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
