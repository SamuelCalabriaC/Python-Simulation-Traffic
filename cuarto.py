import pygame
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
from pared import Pared

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

        self.semaforos = [self.semaforo_fruteria,self.semaforo_maragalltelefonicaop,self.semaforo_maragalltelefonica,self.semaforo_colemaragall, self.semaforo_tajoanais
                          ,self.semaforo_maragallpunticoma, self.semaforo_samba,self.semaforo_dantecmaragall,self.semaforo_maragallcondis,self.semaforo_maragallcondisop,
                          self.semaforo_dantecolegio, self.semaforo_colegiodante, self.semaforo_bajadadelaplanainicio, self.semaforo_dantebajadadelaplana, self.semaforo_bajadadelaplana,
                          self.semaforo_despueschino, self.semaforo_subidacap, self.semaforo_cap, self.semaforo_cris]


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
                   [483, 323, 72, 20, GRIS],  # MARAGALL DERECHA LUISMI
                   [483, 268, 72, 40, GRIS],  # MARAGALL DERECHA LUISMI

                   [140,98,25,27,GRIS], #PEQUEÑO IZQUIERDA
                   [180,98,25,27,GRIS], #Pequeño derecha


                   [140, 20, 130, 45, GRIS],  # BANCO SABADELL
                   [285,20,165,45,GRIS], #ENTRADA METRO IBIZA
                   [483, 20, 87, 45, GRIS2],  #SAMBA

                   [483, 98, 72, 100, GRIS],  # PUNT I COMA
                   [483, 213, 72, 60, GRIS],  # PUNT I COMA


                   [20, 203, 45, 50, GRIS],  #3 bloque izq (entrada dante)
                   [20,253,20,127,GRIS],  #4 bloque izq. (START COCHES DANTE)

                   [20,268,110,112,GRIS],  #GORDO ABAJO A LA IZQUIERDA
                   [130,268,40,30,GRIS],  #CASA JULIO CESAR
                   [185,268,25,30,GRIS],  #BAR DESPUES CASA JULIO

                   [225,268,65,45,GRIS],  #COLEGIO

                   [305,268,65,60,GRIS],  #INVENTADO DESPUES DEL COLEGIO

                   [385,268,65,60,GRIS], #TRASTEVERE

                   [130,313,80,67,GRIS2],  #ESCALON 1
                   [210,328,80,52,GRIS],  #ESCALON 2
                   [290,343,80,37,GRIS2],  #ESCALON 3
                   [370,358,80,22,GRIS],  #ESCALON 4
                   [385,343,65,15,GRIS]
                   ]

        # Iteramos a través de la lista. Creamos la pared y la añadimos a la lista.
        for item in paredes:
            pared = Pared(item[0], item[1], item[2], item[3], item[4])
            self.pared_lista.add(pared)

    def update_semaforos(self):
        for x in self.semaforos:
            if x.calculo_cambio().__eq__(1) and x not in self.pared_lista:
                self.pared_lista.add(x)
                x.ultimocambio = 0
                x.rojo = 1
            elif x.calculo_cambio().__eq__(1) and x in self.pared_lista:
                self.pared_lista.remove(x)
                x.ultimocambio = 0
                x.rojo = 0