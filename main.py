import random
import threading
import pygame
from protagonista import Protagonista

from interseccion import Interseccion
from cuarto import Cuarto1
import os
from redN import Neural_net

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
    for semafor in cuarto1.semaforos_con_gente:
        if semafor.get_Rojo() == 1:
            semafor.nCoches += random.randint(0, 3)
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
                semafor.nPeatones -= random.randint(2, 4)
            if semafor.tPeatones > 1:
                semafor.tPeatones -= 1
        else:
            semafor.ultimocambio += 1
            semafor.nPeatones += random.randint(0, 5)
            if semafor.nPeatones > 0:
                semafor.tPeatones += 1
            if semafor.nPeatones == 0:
                semafor.tPeatones = 0

            if semafor.nCoches > 2:
                semafor.nCoches -= random.randint(1, 3)
            elif 0 < semafor.nCoches < 2:
                semafor.nCoches -= 1

            if semafor.tCoches > 1:
                semafor.tCoches -= 2
            if semafor.t1Coche > 1:
                semafor.t1Coche -= 1

    for sem in cuarto1.semaforos_sin_gente:
        if sem.get_Rojo() == 1:
            sem.nCoches += random.randint(0, 3)
            if sem.nCoches > 0:
                sem.tCoches += 2
                sem.t1Coche += 1
            if sem.nCoches == 0:
                if sem.tCoches > 5:
                    sem.tCoches -= 5
                    sem.t1Coche = 0
                else:
                    sem.tCoches = 0
                    sem.t1Coche = 0
        else:
            if sem.nCoches > 2:
                sem.nCoches -= random.randint(1, 3)
            if sem.tCoches > 1:
                sem.tCoches -= 2
            if sem.t1Coche > 1:
                sem.t1Coche -= 1

def getSemaforosStatic(cuarto1):
    listaCruces = [(cuarto1.semaforo_dantecolegio,cuarto1.semaforo_colegiodante),(cuarto1.semaforo_dantebajadadelaplana,cuarto1.semaforo_bajadadelaplanainicio),
                   (cuarto1.semaforo_dantecmaragall,cuarto1.semaforo_maragallcondis),[cuarto1.semaforo_colemaragall],
                   (cuarto1.semaforo_cap,cuarto1.semaforo_subidacap,cuarto1.semaforo_cris),(cuarto1.semaforo_bajadadelaplana,cuarto1.semaforo_despueschino,cuarto1.semaforo_fruteria),
                   (cuarto1.semaforo_tajoanais, cuarto1.semaforo_tajoanais, cuarto1.semaforo_samba)]
    for i in listaCruces:
        print(i)
        if(len(i) == 2):
            calle1Cruce1 = i[0].calculo_cambio2()
            calle2Cruce1 = i[1].calculo_cambio2()

            if(calle1Cruce1 !=0 and calle2Cruce1 == 0):
                i[0].setRojo(0)
                i[1].setRojo(1)
            elif(calle1Cruce1 == 0 and calle2Cruce1 != 0):
                i[0].setRojo(1)
                i[1].setRojo(0)
            elif(calle1Cruce1 != 0 and calle2Cruce1 != 0):
                if(calle1Cruce1 < calle1Cruce1):
                    i[0].setRojo(0)
                    i[1].setRojo(1)
                else:
                    i[0].setRojo(1)
                    i[1].setRojo(0)
            else:
                i[0].setRojo(1)
                i[1].setRojo(1)
        if(len(i) == 1):
            calle1Cruce1 = i[0].calculo_cambio2()
            if(calle1Cruce1 == 0):
                i[0].setRojo(1)
            else:
                i[0].setRojo(0)
        if(len(i) == 3):
            if (len(i) == 2):
                calle1Cruce1 = i[0].calculo_cambio2()
                calle2Cruce1 = max(i[1].calculo_cambio2(),i[2].calculo_cambio2())
                if (calle1Cruce1 != 0 and calle2Cruce1 == 0):
                    i[0].setRojo(0)
                    i[1].setRojo(1)
                    i[2].setRojo(1)
                elif (calle1Cruce1 == 0 and calle2Cruce1 != 0):
                    i[0].setRojo(1)
                    i[1].setRojo(0)
                    i[2].setRojo(0)
                elif (calle1Cruce1 != 0 and calle2Cruce1 != 0):
                    if (calle1Cruce1 < calle1Cruce1):
                        i[0].setRojo(0)
                        i[1].setRojo(1)
                        i[2].setRojo(1)
                    else:
                        i[0].setRojo(1)
                        i[1].setRojo(0)
                        i[2].setRojo(0)
                else:
                    i[0].setRojo(1)
                    i[1].setRojo(1)
                    i[2].setRojo(1)

def getPredictionSemafors(cuarto1):
    # Dante Can Mateu
    dantecanmateu = neuralnet.prediction(cuarto1.semaforo_dantecolegio.get_Values())
    canmateudante = neuralnet.prediction(cuarto1.semaforo_colegiodante.get_Values())
    # print("Valores Dante: "+str(cuarto1.semaforo_dantecolegio.get_Values())+" with value -> "+str(a))
    # print("Valores Cole"+str(cuarto1.semaforo_colegiodante.get_Values())+" with value ->"+str(b))
    # print()
    if dantecanmateu > canmateudante:
        cuarto1.semaforo_dantecolegio.setRojo(0)
        cuarto1.semaforo_colegiodante.setRojo(1)
    else:
        cuarto1.semaforo_dantecolegio.setRojo(1)
        cuarto1.semaforo_colegiodante.setRojo(0)

    # Bajada de la plana Dante
    dantebajada = neuralnet.prediction(cuarto1.semaforo_dantebajadadelaplana.get_Values())
    bajadadante = neuralnet.prediction(cuarto1.semaforo_bajadadelaplanainicio.get_Values())
    if dantebajada > bajadadante:
        cuarto1.semaforo_dantebajadadelaplana.setRojo(0)
        cuarto1.semaforo_bajadadelaplanainicio.setRojo(1)
    else:
        cuarto1.semaforo_dantebajadadelaplana.setRojo(1)
        cuarto1.semaforo_bajadadelaplanainicio.setRojo(0)

    # Dante Maragall
    dantemaragall = neuralnet.prediction(cuarto1.semaforo_dantecmaragall.get_Values())
    maragalldante = neuralnet.prediction(cuarto1.semaforo_maragallcondis.get_Values())

    if dantemaragall > 0.80 and dantemaragall > maragalldante:
        cuarto1.semaforo_dantecmaragall.setRojo(0)
        cuarto1.semaforo_maragallcondis.setRojo(1)
        cuarto1.semaforo_maragallcondisop.setRojo(1)
    else:
        cuarto1.semaforo_dantecmaragall.setRojo(1)
        cuarto1.semaforo_maragallcondis.setRojo(0)
        cuarto1.semaforo_maragallcondisop.setRojo(0)

    # Granollers Maragall
    granollers = neuralnet.prediction(cuarto1.semaforo_colemaragall.get_Values())
    # maragallTelefonica = neuralnet.prediction(cuarto1.semaforo_maragalltelefonica.get_Values())
    # maragallOp = neuralnet.prediction(cuarto1.semaforo_maragalltelefonicaop.get_Values())
    if granollers > 0.90:
        cuarto1.semaforo_colemaragall.setRojo(0)
        cuarto1.semaforo_maragalltelefonica.setRojo(1)
        cuarto1.semaforo_maragalltelefonicaop.setRojo(1)
    else:
        cuarto1.semaforo_colemaragall.setRojo(1)
        cuarto1.semaforo_maragalltelefonica.setRojo(0)
        cuarto1.semaforo_maragalltelefonicaop.setRojo(0)

    # Tajo Inicio
    cap = neuralnet.prediction(cuarto1.semaforo_cap.get_Values())
    subidacap = neuralnet.prediction(cuarto1.semaforo_subidacap.get_Values())
    rieras = neuralnet.prediction(cuarto1.semaforo_cris.get_Values())

    if subidacap > 0.90 and rieras < cap:
        cuarto1.semaforo_cap.setRojo(0)
        cuarto1.semaforo_cris.setRojo(1)
        cuarto1.semaforo_subidacap.setRojo(0)
    elif subidacap > 0.90 and rieras >= cap:
        cuarto1.semaforo_cap.setRojo(1)
        cuarto1.semaforo_cris.setRojo(0)
        cuarto1.semaforo_subidacap.setRojo(0)
    else:
        cuarto1.semaforo_cap.setRojo(0)
        cuarto1.semaforo_cris.setRojo(0)
        cuarto1.semaforo_subidacap.setRojo(1)

    # Tajo Bajada de la Plana
    finalbajada = neuralnet.prediction(cuarto1.semaforo_bajadadelaplana.get_Values())
    chino = neuralnet.prediction(cuarto1.semaforo_despueschino.get_Values())
    fruteria = neuralnet.prediction(cuarto1.semaforo_fruteria.get_Values())

    if finalbajada > 0.90:
        if chino >= fruteria:
            cuarto1.semaforo_bajadadelaplana.setRojo(0)
            cuarto1.semaforo_despueschino.setRojo(0)
            cuarto1.semaforo_fruteria.setRojo(1)
        else:
            cuarto1.semaforo_bajadadelaplana.setRojo(0)
            cuarto1.semaforo_despueschino.setRojo(1)
            cuarto1.semaforo_fruteria.setRojo(0)
    else:
        cuarto1.semaforo_bajadadelaplana.setRojo(1)
        cuarto1.semaforo_despueschino.setRojo(0)
        cuarto1.semaforo_fruteria.setRojo(0)

    # Tajo Maragall
    tajofinal = neuralnet.prediction(cuarto1.semaforo_tajoanais.get_Values())
    maragallfinal = neuralnet.prediction(cuarto1.semaforo_tajoanais.get_Values())
    samba = neuralnet.prediction(cuarto1.semaforo_samba.get_Values())

    if tajofinal >= maragallfinal and tajofinal >= samba:
        cuarto1.semaforo_tajoanais.setRojo(0)
        cuarto1.semaforo_maragallpunticoma.setRojo(1)
        cuarto1.semaforo_samba.setRojo(1)
    elif samba >= maragallfinal and samba >= tajofinal:
        cuarto1.semaforo_tajoanais.setRojo(1)
        cuarto1.semaforo_maragallpunticoma.setRojo(1)
        cuarto1.semaforo_samba.setRojo(0)
    else:
        cuarto1.semaforo_tajoanais.setRojo(1)
        cuarto1.semaforo_maragallpunticoma.setRojo(0)
        cuarto1.semaforo_samba.setRojo(1)
        
    return 0


def escribirsemaforos(cuarto1):
    with open('data/data.txt', 'w') as file:
        file.write("PeatonesDante "+str(cuarto1.semaforo_dantecolegio.nPeatones)+"\n")
        file.write("CochesDante " + str(cuarto1.semaforo_dantecolegio.nCoches)+"\n")
        file.write("PeatonesMateu " + str(cuarto1.semaforo_colegiodante.nPeatones) + "\n")
        file.write("CochesMateu " + str(cuarto1.semaforo_colegiodante.nCoches) + "\n")


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
            #getPredictionSemafors(cuarto1)
            getSemaforosStatic(cuarto1)
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


# Edit Configurations, Add new Paralel Configuration, data.py main.py
if __name__ == "__main__":
    thread1 = threading.Thread(target=run())
    thread1.start()

# Fin
