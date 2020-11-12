import random
import threading
import pygame
from protagonista import Protagonista
import matplotlib
from interseccion import Interseccion
from cuarto import Cuarto1
import os
import numpy as np
from redN import Neural_net

matplotlib.use("TkAgg")
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
VIOLETA = (255, 0, 255)
GRIS = (150, 152, 154)
GRIS2 = (170, 160, 150)
GRIS3 = (190, 130, 80)
ROSA = (255, 192, 203)

neuralnet = Neural_net()

# Centrar la pantalla del simulador
x = 100
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

def actValuesSemafors(cuarto1):
    for semafor in cuarto1.semaforos:
        if semafor.get_Rojo()==1:
            semafor.nCoches += random.randint(0,3)
            if semafor.nCoches > 0:
                semafor.tCoches += 2
                semafor.t1Coche += 1
            if semafor.nCoches == 0:
                if semafor.tCoches > 5:
                    semafor.tCoches -= 5
                    semafor.t1Coche = 0
                else:
                    semafor.tCoches = 0
                    semafor.t1Coche = 0
            semafor.ultimocambio += 1
            if semafor.nPeatones > 3:
                semafor.nPeatones -= 3
            if semafor.tPeatones > 1:
                semafor.tPeatones -= 1
        else:
            semafor.ultimocambio += 1
            semafor.nPeatones += random.randint(0,5)
            if semafor.nPeatones > 0:
                semafor.tPeatones += 1
            if semafor.nPeatones == 0:
                semafor.tPeatones = 0
            if semafor.nCoches > 0:
                semafor.nCoches -= 2
            if semafor.tCoches > 1:
                semafor.tCoches -= 2
            if semafor.t1Coche > 1:
                semafor.t1Coche -= 1

def getPredictionSemafors(cuarto1):
    a = neuralnet.prediction(cuarto1.semaforo_dantecolegio.get_Values())
    b = neuralnet.prediction(cuarto1.semaforo_colegiodante.get_Values())
    print("Valores Dante: "+str(cuarto1.semaforo_dantecolegio.get_Values())+"with value -> "+str(a))
    print("Valores Cole"+str(cuarto1.semaforo_colegiodante.get_Values())+"with value ->"+str(b))
    print()
    if a > b:
        cuarto1.semaforo_dantecolegio.setRojo(0)
        cuarto1.semaforo_colegiodante.setRojo(1)
    else:
        cuarto1.semaforo_dantecolegio.setRojo(1)
        cuarto1.semaforo_colegiodante.setRojo(0)
    return 0

def escribirsemaforos(cuarto1):
    with open('data/data.txt','w') as file:
        file.write("PeatonesDante "+str(cuarto1.semaforo_dantecolegio.nPeatones)+"\n")
        file.write("CochesDante " + str(cuarto1.semaforo_dantecolegio.nCoches)+"\n")
        file.write("PeatonesMateu " + str(cuarto1.semaforo_colegiodante.nPeatones)+ "\n")
        file.write("CochesMateu " + str(cuarto1.semaforo_colegiodante.nCoches)+ "\n")


def actSemafors(cuarto1):
    for pared in cuarto1.semaforos:
        if pared.get_Rojo().__eq__(1) and (pared not in cuarto1.pared_lista):
            cuarto1.pared_lista.add(pared)
        if pared.get_Rojo().__eq__(0) and (pared in cuarto1.pared_lista):
            cuarto1.pared_lista.remove(pared)
        pared.set_ultimoCambio(0)
        pared.set_t1Coches(0)
    return 0


def run():
    """ Programa Principal """
    # ventanaData = Data() with tk
    # Llamamos a esta función para que la biblioteca Pygame pueda autoiniciarse.
    pantalla = pygame.display.set_mode((590, 400), 0, 32)
    pygame.init()
    pygame.display.set_caption('Simulation IA')
    num_coches = 3
    coches = []

    # Iniciacion de coches.
    for iters in range(0, num_coches):
        salida = random.randint(0, len(Interseccion.listainicios) - 1)
        coche2 = Protagonista(Interseccion.listainicios[salida][0], Interseccion.listainicios[salida][1])
        del Interseccion.listainicios[salida]
        coches.append((coche2, salida))

    desplazarsprites = pygame.sprite.Group()

    for coche in coches:
        if type(coche[0]) == Protagonista:
            desplazarsprites.add(coche[0])

    # Iniciar el cuarto
    cuarto1 = Cuarto1()

    # Iniciar los semaforos
    cuarto1.setSemaforos()

    reloj = pygame.time.Clock()
    hecho = False

    # Crear Parametros semaforos
    cuarto1.setSemaforos()

    iters = 0
    while not hecho:
        cuarto_actual = cuarto1

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

        for coche in coches:
            if type(coche[0]) == Protagonista:
                coche[0].movimiento()

        for coche in coches:
            if type(coche[0]) == Protagonista:
                coche[0].mover(cuarto_actual.pared_lista)

        if iters > 120:
            actValuesSemafors(cuarto1)
            # Calcular los que han de cruzar en rojo
            getPredictionSemafors(cuarto1)
            # Actualizar los que cambien
            actSemafors(cuarto1)
            iters = 0
            escribirsemaforos(cuarto1)

        iters += 1
        # --- Dibujamos ---
        pantalla.fill(BLANCO)
        desplazarsprites.draw(pantalla)
        cuarto_actual.pared_lista.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


#Edit Configurations, Add new Paralel Configuration, data.py main.py
if __name__ == "__main__":
    thread1 = threading.Thread(target=run())
    thread1.start()

# Fin
