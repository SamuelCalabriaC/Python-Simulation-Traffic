import random
import threading
import pygame
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")


NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
VIOLETA = (255, 0, 255)
GRIS = (150,152,154)
GRIS2 = (170,160,150)
GRIS3 = (190,130,80)
ROSA = (255,192,203)

#Centrar la pantalla del simulador
x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


class Interseccion():
    p1 = (450, 65)
    p2 = (65, 65)
    p3 = (20, 65)
    p4 = (65, 83)
    p5 = (468, 65)
    p6 = (450, 83)
    p7 = (468, 83)
    p8 = (468, 198)
    p9 = (450, 253)
    p10 = (468, 253)
    p11 = (468, 308)
    p12 = (450, 328)
    p13 = (468, 328)
    p14 = (370, 342)
    p15 = (370, 328)
    p16 = (290, 328)
    p17 = (210, 313)
    p18 = (210, 253)
    p19 = (170, 253)
    p20 = (170, 298)
    p21 = (140, 298)
    p22 = (125, 253)
    p23 = (65, 188)
    p24 = (65, 253)
    p25 = (125, 188)
    p26 = (125, 83)
    p27 = (125, 65)
    p28 = (165, 83)
    p29 = (205, 83)
    p30 = (270, 83)
    p31 = (270, 65)
    p32 = (205, 125)
    p33 = (165, 125)
    p34 = (125, 125)
    p35 = (555, 198)
    p36 = (555, 308)
    p38 = (40, 253)
    p39 = (210, 298)
    p40 = (290, 313)
    p41 = (290, 253)
    p42 = (370, 253)
    p43 = (270, 20)
    p44 = (450, 20)
    p45 = (468, 20)
    p46 = (555, 65)
    p47 = (555, 83)
    p48 = (125, 20)
    p49 = (20, 188)
    p50 = (20, 83)
    p51 = (450, 365)
    p52 = (468, 365)
    pfinal = (555,345)

    listainicios = [p48,p43,p44,p45,p14,p21,p38,p49,p50,p52]

class Pared(pygame.sprite.Sprite):
    """Esta clase representa la barra inferior que controla el protagonista """

    def __init__(self, x, y, largo, alto, color):
        """ Función Constructor """

        # Llama al constructor padre
        super().__init__()

        # Crea una pared AZUL, con las dimensiones especificadas en los parámetros
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)

        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa la barra inferior que controla el
    protagonista """

    # Establecemos el vector velocidad
    cambio_x = 0
    cambio_y = 0
    lastmove = 99
    def __init__(self, x, y):
        """ Función Constructor """

        # Llama al constructor padre
        super().__init__()

        # Establecemos el alto y largo
        self.image = pygame.Surface([15, 15])
        self.image.fill((0,166,214))

        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def cambiovelocidad(self, x, y):
        """ Cambia la velocidad del protagonista. Es llamada con una pulsación del teclado. """
        self.cambio_x += x
        self.cambio_y += y

    def stop(self):
        self.cambio_x = 0
        self.cambio_y = 0

    def mover(self, paredes):
        """ Encuentra una nueva posición para el protagonista """

        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x

        # Hemos chocado contra la pared después de esta actualización?
        lista_impactos_bloques = pygame.sprite.spritecollide(self, paredes, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado.
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            else:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right

        # Desplazar arriba/izquierda
        self.rect.y += self.cambio_y

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, paredes, False)
        for bloque in lista_impactos_bloques:

            # Reseteamos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top
            else:
                self.rect.top = bloque.rect.bottom


    def getPos(self):
        return (self.rect.x,self.rect.y)

    def setPos(self,pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    #Arriba 1
    #Abajo 2
    #Izquierda 3
    #Derecha 4
    def movimiento(self):
        pos = self.getPos()

        if (pos.__eq__(Interseccion.pfinal)):
            self.lastmove = 99
            self.stop()
            self.setPos(Interseccion.p48)



        #Finales
        if (((pos.__eq__(Interseccion.p3)) or (pos.__eq__(Interseccion.p50))  or (pos.__eq__(Interseccion.p49)) or (pos.__eq__(Interseccion.p38)) or (pos.__eq__(Interseccion.p21)) or
            (pos.__eq__(Interseccion.p14)) or (pos.__eq__(Interseccion.p48)) or (pos.__eq__(Interseccion.p43)) or
            (pos.__eq__(Interseccion.p44)) or (pos.__eq__(Interseccion.p45))or (pos.__eq__(Interseccion.p43)) or (pos.__eq__(Interseccion.p48)) or (pos.__eq__(Interseccion.p44))
                or (pos.__eq__(Interseccion.p45)) or (pos.__eq__(Interseccion.p51)) or (pos.__eq__(Interseccion.p52))) and (self.lastmove != 99)):
            #TP hacia alguna direccion
            self.lastmove = 99
            self.stop()
            self.setPos(Interseccion.p14)
            pass

        elif (pos.__eq__(Interseccion.p21)):
            self.stop()
            self.cambiovelocidad(1,0)
            self.lastmove = 4

        #Cuando hay Tps se puede mover un poco
        elif (pos.__eq__(Interseccion.p14) or pos.__eq__((370,343)) or pos.__eq__((370,345))):
            if (self.lastmove==99):
                #self.stop()
                self.cambiovelocidad(0,-1)
                self.lastmove = 1
            else:
                self.cambiovelocidad(0,-1)
                self.lastmove = 1

        #Comienzos
        elif ((pos.__eq__(Interseccion.p3) or pos.__eq__(Interseccion.p50)  or pos.__eq__(Interseccion.p49) or pos.__eq__(Interseccion.p38) or
            pos.__eq__(Interseccion.p17) or pos.__eq__(Interseccion.p16)) and self.lastmove==99):
            self.cambiovelocidad(1,0)
            self.lastmove = 4
            pass

        #Nodo 2
        elif (pos.__eq__(Interseccion.p2)):
            k = random.randint(0, 1)
            if (k==0):
                self.stop()
                self.cambiovelocidad(0,1)
                self.lastmove = 2
            else:
                pass
                self.lastmove = 3

        #Nodo 4
        elif (pos.__eq__(Interseccion.p4)):
            k = random.randint(0, 1)
            #k = 0 seguir el camino de abajo
            if (k==0):
                if (self.lastmove.__eq__(2)):
                    self.lastmove = 2
                    pass
                elif (self.lastmove.__eq__(4)):
                    self.stop()
                    self.cambiovelocidad(0,1)
                    self.lastmove = 2
            #k = 1 seguir el camino de Tajo
            else:
                if (self.lastmove.__eq__(4)):
                    self.lastmove = 4
                    pass
                elif(self.lastmove.__eq__(2)):
                    self.stop()
                    self.cambiovelocidad(1,0)
                    self.lastmove = 4

        #Nodo 23 y Nodo 24
        elif (pos.__eq__(Interseccion.p23) or pos.__eq__(Interseccion.p24)):
            k = random.randint(0,1)
            # K = 0 hacia dante.
            if ( k == 0 ):
                if (self.lastmove.__eq__(2)):
                    self.lastmove = 2
                if (self.lastmove.__eq__(4)):
                    self.stop()
                    self.cambiovelocidad(0,1)
                    self.lastmove = 2

            # K = 1 hacia bajada de la plana
            if ( k == 1 ):
                if (self.lastmove.__eq__(4)):
                    self.lastmove = 4
                    pass
                if (self.lastmove.__eq__(2)):
                    self.stop()
                    self.cambiovelocidad(1,0)
                    self.lastmove = 4

        #Nodo 22
        elif (pos.__eq__(Interseccion.p22)):
            k = random.randint(0,1)
            # Sigue por Dante
            if ( k == 0 ):
                self.lastmove = 4
            else:
                self.stop()
                self.cambiovelocidad(0,-1)
                self.lastmove = 1

        #Nodo 25
        elif (pos.__eq__(Interseccion.p25)):
            if (self.lastmove.__eq__(1)):
                self.lastmove = 1
            else:
                self.stop()
                self.cambiovelocidad(0,-1)
                self.lastmove = 3

        #Nodo 34
        elif (pos.__eq__(Interseccion.p34)):
            if (self.lastmove.__eq__(3)):
                self.stop()
                self.cambiovelocidad(0,-1)
                self.lastmove = 1
            elif (self.lastmove.__eq__(1)):
                self.lastmove = 1

        #Nodo 27
        elif (pos.__eq__(Interseccion.p27)):
            if (self.lastmove.__eq__(3)):
                self.lastmove = 3
            if (self.lastmove.__eq__(2)):
                self.stop()
                self.cambiovelocidad(-1,0)
                self.lastmove = 3
            if (self.lastmove.__eq__(1)):
                self.stop()
                self.cambiovelocidad(-1,0)
                self.lastmove = 3

        #Nodo 26
        elif (pos.__eq__(Interseccion.p26)):
            k = random.randint(0,1)
            # k = 0 Ir hacia tajo derecha
            if k.__eq__(0):
                if (self.lastmove.__eq__(1)):
                    self.stop()
                    self.cambiovelocidad(1,0)
                    self.lastmove = 4
                if (self.lastmove.__eq__(4)):
                    self.lastmove = 4
            else:
                if (self.lastmove.__eq__(1)):
                    self.lastmove = 1
                if (self.lastmove.__eq__(4)):
                    pass
                    self.lastmove = 4

        #Nodo 28 & 29
        elif (pos.__eq__(Interseccion.p28) or pos.__eq__(Interseccion.p29)):
            k = random.randint(0,1)
            #K=0 seguir Tajo
            if (k==0):
                self.lastmove = 4
                pass
            else:
                self.stop()
                self.cambiovelocidad(0,1)
                self.lastmove = 2

        #Nodo 32
        elif (pos.__eq__(Interseccion.p32)):
            self.stop()
            self.cambiovelocidad(-1,0)
            self.lastmove = 3

        #Nodo 33
        elif (pos.__eq__(Interseccion.p33)):
            if (self.lastmove.__eq__(3)):
                self.lastmove = 3
                pass
            if (self.lastmove.__eq__(2)):
                self.stop()
                self.cambiovelocidad(-1,0)
                self.lastmove = 3

        #Nodo 31
        elif (pos.__eq__(Interseccion.p31)):
            k = random.randint(0,1)
            # k = 0 seguimos por tajo arriba
            if (k==0):
                if (self.lastmove.__eq__(3)):
                    self.lastmove = 3
                elif (self.lastmove.__eq__(2)):
                    self.stop()
                    self.cambiovelocidad(-1,0)
                    self.lastmove = 3
            # K = 1 vamos hacia tajo por abajo
            if (k==1):
                if (self.lastmove.__eq__(4)):
                    self.lastmove = 4
                elif (self.lastmove.__eq__(2)):
                    self.stop()
                    self.cambiovelocidad(1,0)
                    self.lastmove = 4

        #Nodo 30
        elif (pos.__eq__(Interseccion.p30)):
            if (self.lastmove.__eq__(2)):
                self.stop()
                self.cambiovelocidad(1,0)
                self.lastmove = 4
            elif (self.lastmove.__eq__(4)):
                pass
                self.lastmove = 4

        #Nodos comienzo hacia abajo 48,43,44,45

        elif ((pos.__eq__(Interseccion.p48)) or (pos.__eq__(Interseccion.p43)) or (pos.__eq__(Interseccion.p44)) or (pos.__eq__(Interseccion.p45))):
            self.cambiovelocidad(0,1)
            self.lastmove = 2

        #Cruce plaza Ibiza

        #Nodo 1
        elif (pos.__eq__(Interseccion.p1)):
            if (self.lastmove.__eq__(2)):
                self.stop()
                self.cambiovelocidad(-1,0)
                self.lastmove = 3
            elif (self.lastmove.__eq__(3)):
                self.lastmove = 3
                pass
            else:
                self.stop()
                self.cambiovelocidad(-1, 0)
                self.lastmove = 3

        #Nodo 5
        elif (pos.__eq__(Interseccion.p5)):
            k = random.randint(0,1)
            # K = 0 plaza ibiza (recto)
            if (k==0):
                if (self.lastmove.__eq__(1)):
                    self.lastmove = 1
                    pass
                elif (self.lastmove.__eq__(3)):
                    self.stop()
                    self.cambiovelocidad(0,-1)
                    self.lastmove = 1
            # K = 1 tajo
            elif (k==1):
                if (self.lastmove.__eq__(1)):
                    self.stop()
                    self.cambiovelocidad(-1,0)
                    self.lastmove == 3
                elif (self.lastmove.__eq__(3)):
                    self.lastmove == 3

        #Nodo 6
        elif (pos.__eq__(Interseccion.p6)):
            k = random.randint(0,1)
            # K = 0 hacia pasate (derecha)
            if k == 0:
                self.lastmove = 4
            # K = 1 hacia pans (abajo)
            else:
                self.stop()
                self.cambiovelocidad(0,1)
                self.lastmove = 2

        #Nodo 7
        elif (pos.__eq__(Interseccion.p7)):
            k = random.randint(0,1)
            #k=0 hacia pasate (derecha)
            if k==0:
                if (self.lastmove.__eq__(4)):
                    self.lastmove = 4
                elif (self.lastmove.__eq__(1)):
                    self.stop()
                    self.cambiovelocidad(1,0)
                    self.lastmove = 4
            #k=1 hacia plaza ibiza
            else:
                if (self.lastmove.__eq__(1)):
                    self.lastmove = 1
                elif (self.lastmove.__eq__(4)):
                    self.stop()
                    self.cambiovelocidad(0,-1)
                    self.lastmove = 1

        #Nodo 47
        elif (pos.__eq__(Interseccion.p47)):
            k = random.randint(0,1)
            #Hacia abajo
            if (k==0):
                self.stop()
                self.cambiovelocidad(0,1)
                self.lastmove = 2
            #Hacia arriba
            else:
                self.stop()
                self.cambiovelocidad(0,-1)
                self.lastmove = 1

        #Nodo 46
        elif (pos.__eq__(Interseccion.p46)):
            self.stop()
            self.cambiovelocidad(-1,0)
            self.lastmove= 3

        #Nodo 35
        elif (pos.__eq__(Interseccion.p35) or pos.__eq__(Interseccion.p36)):
            k = random.randint(0,1)
            #0 seguir hacia abajo
            if k==0:
                self.lastmove = 2
                pass
            else:
                self.stop()
                self.cambiovelocidad(-1,0)
                self.lastmove= 3

        #Nodos 52
        elif (pos.__eq__(Interseccion.p52)):
            self.cambiovelocidad(0,-1)
            self.lastmove = 1

        #Nodos 11 y 8
        elif(pos.__eq__(Interseccion.p11) or pos.__eq__(Interseccion.p8)):
            if (self.lastmove.__eq__(1)):
                self.lastmove = 1
                pass
            elif (self.lastmove.__eq__(3)):
                self.stop()
                self.cambiovelocidad(0,-1)
                self.lastmove = 1

        #Nodos 9 y 12
        elif (pos.__eq__(Interseccion.p9) or pos.__eq__(Interseccion.p12)):
            k = random.randint(0,1)
            #k = 0 seguimos maragall abajo
            if k==0:
                if (self.lastmove.__eq__(4)):
                    self.stop()
                    self.cambiovelocidad(0,1)
                    self.lastmove = 2
                if (self.lastmove.__eq__(2)):
                    self.lastmove = 2
            #k=1 cruza de acera
                if (self.lastmove.__eq__(4)):
                    self.lastmove = 4
                elif (self.lastmove.__eq__(2)):
                    self.stop()
                    self.cambiovelocidad(1,0)
                    self.lastmove= 4

        #Nodos 13 y 10
        elif (pos.__eq__(Interseccion.p13) or pos.__eq__(Interseccion.p10)):
            if (self.lastmove.__eq__(4)):
                self.stop()
                self.cambiovelocidad(0,-1)
                self.lastmove = 1
            else:
                self.lastmove = 1

        #Nodo 19
        elif (pos.__eq__(Interseccion.p19)):
            k = random.randint(0,1)
            #Baja
            if (k==0):
                self.stop()
                self.cambiovelocidad(0,1)
                self.lastmove = 2
            else:
                self.lastmove = 4
                pass

        #Nodo 20
        elif (pos.__eq__(Interseccion.p20)):
            if (self.lastmove.__eq__(2)):
                self.stop()
                self.cambiovelocidad(1,0)
                self.lastmove = 4
            else:
                self.lastmove = 4
                pass

        #Nodo 18
        elif (pos.__eq__(Interseccion.p18)):
            if (self.lastmove.__eq__(1)):
                self.stop()
                self.cambiovelocidad(1,0)
                self.lastmove = 4
            else:
                self.lastmove = 4

        #Nodo 39
        elif (pos.__eq__(Interseccion.p39)):
            if (self.lastmove.__eq__(1)):
                self.lastmove = 1
                pass
            else:
                self.stop()
                self.cambiovelocidad(0,-1)
                self.lastmove = 1

        #Nodo 17
        elif (pos.__eq__(Interseccion.p17)):
            self.stop()
            self.cambiovelocidad(0,-1)
            self.lastmove = 1

        elif (pos.__eq__(Interseccion.p41) or pos.__eq__(Interseccion.p42)):
            k = random.randint(0,1)
            if k==0:
                self.lastmove = 4
                pass
            else:
                self.stop()
                self.cambiovelocidad(0,1)
                self.lastmove = 2

        elif (pos.__eq__(Interseccion.p40)):
            k = random.randint(0,1)
            if k==0:
                self.lastmove = 2
                pass
            else:
                self.stop()
                self.cambiovelocidad(-1,0)
                self.lastmove = 3

        elif (pos.__eq__(Interseccion.p16)):
            self.stop()
            self.cambiovelocidad(1,0)
            self.lastmove = 4

        elif (pos.__eq__(Interseccion.p15)):
            k = random.randint(0,1)
            #k = 0 ->12
            if k==0:
                if (self.lastmove.__eq__(2)):
                    self.stop()
                    self.cambiovelocidad(1,0)
                    self.lastmove = 4
                elif (self.lastmove.__eq__(1)):
                    self.stop()
                    self.cambiovelocidad(1,0)
                    self.lastmove = 4
                else:
                    #Viene de la derecha
                    self.lastmove = 4
            else:
                if (self.lastmove.__eq__(2)):
                    self.lastmove = 2
                elif (self.lastmove.__eq__(1)):
                    self.stop()
                    self.cambiovelocidad(0,1)
                    self.lastmove = 2
                else:
                    self.stop()
                    self.cambiovelocidad(0,1)
                    self.lastmove = 2

        elif (pos.__eq__(Interseccion.p42)):
            k = random.randint(0,1)
            if k==0:
                self.lastmove = 4
            else:
                self.stop()
                self.cambiovelocidad(0,1)
                self.lastmove = 2


class Cuarto():
    """ Clase base para todos los cuartos. """

    # Cada cuarto tiene una lista de paredes, y de los sprites enemigos.
    pared_lista = None
    sprites_enemigos = None

    def __init__(self):
        """ Constructor, creamos nuestras listas. """
        self.pared_lista = pygame.sprite.Group()
        self.sprites_enemigos = pygame.sprite.Group()


class Cuarto1(Cuarto):
    """Esto crea todas las paredes del cuarto 1"""
    def __init__(self):

        #Cruze cap
        self.semaforo_fruteria = Pared(140,65,2,15,ROJO)
        self.semaforo_cris = Pared(80,65,2,15,ROJO)
        self.semaforo_cap = Pared(63,83,2,15,ROJO)
        self.semaforo_subidacap = Pared(65,98,15,2,ROJO)

        #cruze bajada de la plana
        self.semaforo_bajadadelaplana = Pared(125,98,15,2,ROJO)
        self.semaforo_despueschino = Pared(123,83,2,15,ROJO)

        #cruze dante bajada
        self.semaforo_bajadadelaplanainicio = Pared(125,251,15,2,ROJO)
        self.semaforo_dantebajadadelaplana = Pared(123,253,2,15,ROJO)

        #cruze colegio
        self.semaforo_dantecolegio = Pared(208,253,2,15,ROJO)
        self.semaforo_colegiodante = Pared(210,268,15,2,ROJO)

        #CRUZE DANTE MARAGALL
        self.semaforo_dantecmaragall = Pared(448,253,2,15,ROJO)
        self.semaforo_maragallcondis = Pared(450,251,15,2,ROJO)
        self.semaforo_maragallcondisop = Pared(468,268,15,2,ROJO)

        #cruze dante tajo
        self.semaforo_maragallpunticoma = Pared(468,98,15,2,ROJO)
        self.semaforo_tajoanais = Pared(448,83,2,15,ROJO)
        self.semaforo_samba = Pared(483,65,2,15,ROJO)


        #CRUZE GRANOLLERS/MARAGALL
        self.semaforo_colemaragall = Pared(448,328,2,15,ROJO)
        self.semaforo_maragalltelefonica = Pared(450,326,15,2,ROJO)
        self.semaforo_maragalltelefonicaop = Pared(468,343,15,2,ROJO)



        super().__init__()
        # Crear las paredes. (x_pos, y_pos, largo, alto)

        # Esta es la lista de las paredes. Cada una se especifica de la forma [x, y, largo, alto]
        paredes = [
                    #MARGENES
                   [0, 0, 20, 760, NEGRO],
                   [570, 0, 20, 400, NEGRO],
                   [0,0,590,20,NEGRO],
                   [0,380,590,40,NEGRO],


                   [20,20,105,45,GRIS],  #ARRIBA IZQUIERDA
                   [20,98,45,90,GRIS],  #2 bloque izq

                   [80,98,45,90,GRIS], # Entre bajada de la plana y subida del cap
                   [80, 203, 45, 50, GRIS], # Estanco, delante de la Marina
                   [140,140,310,113,GRIS], #Mercado de Horta zona cole
                   [220,98,230,50,GRIS], #Mercado de Horta zona tajo

                    #DISCONTINUAS
                   [465,98,3,155,NEGRO],  #DISCONTINUA MARAGALL
                   [465, 268, 3,60, NEGRO],  # DISCONTINUA MARAGALL
                   [465, 343, 3, 40, NEGRO],  # DISCONTINUA MARAGALL
                   [140, 80, 130, 3, NEGRO],  # DISCONTINUA
                   [80, 80, 45, 3, NEGRO],  # DISCONTINUA
                   [483, 80, 72, 3, NEGRO],  # DISCONTINUA
                   [285, 80, 165, 3, NEGRO],  # DISCONTINUA
                   [20, 80, 45, 3, NEGRO],  # DISCONTINUA CRUZE ARRIBA IZQUIERDA

                    [483, 343, 87, 37, GRIS],  # MARAGALL DERECHA LUISMI
                   [483, 323, 72, 20, ROSA],  # MARAGALL DERECHA LUISMI
                   [483, 268, 72, 40, GRIS],  # MARAGALL DERECHA LUISMI

                   [140,98,25,27,GRIS], #PEQUEÑO IZQUIERDA
                   [180,98,25,27,GRIS], #Pequeño derecha


                   [140, 20, 130, 45, GRIS],  # BANCO SABADELL
                   [285,20,165,45,GRIS], #ENTRADA METRO IBIZA
                   [483, 20, 87, 45, GRIS2],  #SAMBA

                   [483, 98, 72, 100, ROSA],  # PUNT I COMA
                   [483, 213, 72, 60, GRIS],  # PUNT I COMA


                   [20, 203, 45, 50, GRIS],  #3 bloque izq (entrada dante)
                   [20,253,20,127,GRIS],  #4 bloque izq. (START COCHES DANTE)

                   [20,268,110,112,GRIS],  #GORDO ABAJO A LA IZQUIERDA
                   [130,268,40,30,GRIS],  #CASA JULIO CESAR
                   [185,268,25,30,GRIS],  #BAR DESPUES CASA JULIO

                   [225,268,65,45,GRIS],  #COLEGIO

                   [305,268,65,60,GRIS],  #INVENTADO DESPUES DEL COLEGIO

                   [385,268,65,60,ROSA], #TRASTEVERE

                   [130,313,80,67,GRIS3],  #ESCALON 1
                   [210,328,80,52,GRIS],  #ESCALON 2
                   [290,343,80,37,GRIS2],  #ESCALON 3
                   [370,358,80,22,GRIS],  #ESCALON 4
                   [385,343,65,15,ROSA]
                   ]

        # Iteramos a través de la lista. Creamos la pared y la añadimos a la lista.
        for item in paredes:
            pared = Pared(item[0], item[1], item[2], item[3], item[4])
            self.pared_lista.add(pared)

    def update_add(self):
        self.pared_lista.add(self.semaforo_cris)
        self.pared_lista.add(self.semaforo_cap)
        self.pared_lista.add(self.semaforo_subidacap)
        self.pared_lista.add(self.semaforo_bajadadelaplana)
        self.pared_lista.add(self.semaforo_despueschino)
        self.pared_lista.add(self.semaforo_bajadadelaplanainicio)
        self.pared_lista.add(self.semaforo_dantebajadadelaplana)
        self.pared_lista.add(self.semaforo_dantecolegio)
        self.pared_lista.add(self.semaforo_colegiodante)
        self.pared_lista.add(self.semaforo_dantecmaragall)
        self.pared_lista.add(self.semaforo_maragallcondis)
        self.pared_lista.add(self.semaforo_maragallcondisop)
        self.pared_lista.add(self.semaforo_maragallpunticoma)
        self.pared_lista.add(self.semaforo_tajoanais)
        self.pared_lista.add(self.semaforo_colemaragall)
        self.pared_lista.add(self.semaforo_maragalltelefonica)
        self.pared_lista.add(self.semaforo_maragalltelefonicaop)
        self.pared_lista.add(self.semaforo_samba)
        self.pared_lista.add(self.semaforo_fruteria)

    def update_del(self):
        self.pared_lista.remove(self.semaforo_cris)
        self.pared_lista.remove(self.semaforo_cap)
        self.pared_lista.remove(self.semaforo_subidacap)
        self.pared_lista.remove(self.semaforo_bajadadelaplana)
        self.pared_lista.remove(self.semaforo_despueschino)
        self.pared_lista.remove(self.semaforo_bajadadelaplanainicio)
        self.pared_lista.remove(self.semaforo_dantebajadadelaplana)
        self.pared_lista.remove(self.semaforo_dantecolegio)
        self.pared_lista.remove(self.semaforo_colegiodante)
        self.pared_lista.remove(self.semaforo_dantecmaragall)
        self.pared_lista.remove(self.semaforo_maragallcondis)
        self.pared_lista.remove(self.semaforo_maragallcondisop)
        self.pared_lista.remove(self.semaforo_maragallpunticoma)
        self.pared_lista.remove(self.semaforo_tajoanais)
        self.pared_lista.remove(self.semaforo_colemaragall)
        self.pared_lista.remove(self.semaforo_maragalltelefonica)
        self.pared_lista.remove(self.semaforo_maragalltelefonicaop)
        self.pared_lista.remove(self.semaforo_samba)
        self.pared_lista.remove(self.semaforo_fruteria)

def run():
    """ Programa Principal """
    #ventanaData = Data() with tk
    # Llamamos a esta función para que la biblioteca Pygame pueda autoiniciarse.
    pantalla = pygame.display.set_mode((590, 400), 0, 32)
    pygame.init()
    pygame.display.set_caption('Simulation IA')
    num_coches = 3
    coches = []

    #Iniciacion de coches.
    for x in range(0,num_coches):
        salida = random.randint(0,len(Interseccion.listainicios)-1)
        coche2 = Protagonista(Interseccion.listainicios[salida][0],Interseccion.listainicios[salida][1])
        del Interseccion.listainicios[salida]
        coches.append((coche2,salida))


    desplazarsprites = pygame.sprite.Group()

    #desplazarsprites.add(protagonista)

    for x in coches:
        if (type(x[0])==Protagonista):
            desplazarsprites.add(x[0])

    cuarto1 = Cuarto1()
    reloj = pygame.time.Clock()
    hecho = False
    cont = 0


    while not hecho:



        cuarto_actual = cuarto1
        # --- Procesamiento de Eventos ---

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    cuarto1.update_add()
                if evento.key == pygame.K_2:
                    cuarto1.update_del()

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_1:
                    cuarto1.update_add()
                if evento.key == pygame.K_2:
                    cuarto1.update_del()

        #Movimientodecoches



        # --- Lógica semaforos en cruze.

        # -- Algoritmo movimiento automatico

        for x in (coches):
            if (type(x[0])==(Protagonista)):
                a = threading.Thread(None, x[0].movimiento())
                a.start()
                a.join()
                #x.movimiento()

        for x in coches:
            if (type(x[0])==(Protagonista)):
                a = threading.Thread(None,x[0].mover(cuarto_actual.pared_lista))
                a.start()
                a.join()
                #x.mover(cuarto_actual.pared_lista)


        # --- Dibujamos ---
        pantalla.fill(BLANCO)
        desplazarsprites.draw(pantalla)
        cuarto_actual.pared_lista.draw(pantalla)
        pygame.display.flip()

        reloj.tick(60)
        cont += 1

    pygame.quit()

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    thread2 = threading.Thread(exec(open("data.py").read()))
    thread2.start()