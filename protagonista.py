import pygame
from interseccion import Interseccion
import random

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
        self.image.fill(ROJO)

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
        print(pos)

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