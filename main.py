import random
import threading
import pygame
import pandas as pd
from protagonista import Protagonista
import tkinter as tk
import matplotlib
from interseccion import Interseccion
from cuarto import Cuarto1, Cuarto

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


def setParamsSemafors(Cuarto1):
    pass


def actParamsSemafors(Cuarto1):
    pass



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
        coche2 = Protagonista(Interseccion.listainicios[salida][0], Interseccion.listainicios[salida][1])
        del Interseccion.listainicios[salida]
        coches.append((coche2,salida))

    desplazarsprites = pygame.sprite.Group()

    for x in coches:
        if (type(x[0])==Protagonista):
            desplazarsprites.add(x[0])

    cuarto1 = Cuarto1()
    reloj = pygame.time.Clock()
    hecho = False

    # Crear Parametros semaforos
    setParamsSemafors(Cuarto1)

    while not hecho:

        cuarto_actual = cuarto1
        # --- Procesamiento de Eventos ---

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    cuarto1.update_semaforos()


            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_1:
                    cuarto1.update_semaforos()

        # --- Lógica semaforos en cruze.

        # -- Algoritmo movimiento automatico

        for x in (coches):
            if (type(x[0])==(Protagonista)):
                x[0].movimiento()

                #x.movimiento()

        for x in coches:
            if (type(x[0])==(Protagonista)):
                x[0].mover(cuarto_actual.pared_lista)
                #x.mover(cuarto_actual.pared_lista)


        #Crear Parametros semaforos
        actParamsSemafors(Cuarto1)


        # --- Dibujamos ---
        pantalla.fill(BLANCO)
        desplazarsprites.draw(pantalla)
        cuarto_actual.pared_lista.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    thread = threading.Thread(exec(open("redN.py").read()))
    thread.start()
    thread1 = threading.Thread(target=run)
    thread1.start()
    thread2 = threading.Thread(exec(open("data.py").read()))
    thread2.start()