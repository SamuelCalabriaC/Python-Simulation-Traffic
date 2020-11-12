from itertools import count
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from cuarto import Cuarto1, Cuarto
from pared import Pared


def graph():
    house = np.random.normal(200000,20000,2000)
    plt.hist(house,200)
    plt.show()
    
def initdata():
    with open('data/data.txt','w') as file:
        file.write("PeatonesDante "+str(0)+"\n")
        file.write("CochesDante " + str(0)+"\n")
        file.write("PeatonesMateu " + str(0)+ "\n")
        file.write("CochesMateu " + str(0)+ "\n")

while True:
    initdata()
    pullData = open("data/data.txt", "r").read()
    dataList = pullData.split('\n')

    data = []
    data2 = []
    data3 = []
    data4 = []
    x_index = []

    index = count()
    plt.style.use('fivethirtyeight')

    def animate(i):
        x_index.append(next(index))
        a = open('data/data.txt', 'r').read()
        lineas = a.split('\n')

        #Settings of graph
        plt.style.use('fivethirtyeight')
        plt.cla()
        plt.ylabel("Number of")
        plt.ylim((0,20))
        plt.xlabel("Time in seconds (s)")
        plt.title("Traffic simulator")

        #1st line
        linea = lineas[0].split(' ')
        nombre = linea[0]
        data.append(int(float(linea[-1])))
        plt.plot(x_index,data, label=nombre)

        #2nd line
        linea = lineas[1].split(' ')
        nombre = linea[0]
        data2.append(int(float(linea[-1])))
        plt.plot(x_index, data2, label=nombre)

        #3rd line
        linea = lineas[2].split(' ')
        nombre = linea[0]
        data3.append(int(float(linea[-1])))
        plt.plot(x_index, data3, label=nombre)

        #4th line
        linea = lineas[3].split(' ')
        nombre = linea[0]
        data4.append(int(float(linea[-1])))
        plt.plot(x_index, data4, label=nombre)

        plt.legend(loc='upper left')
        plt.tight_layout()

    ani = FuncAnimation(plt.gcf(),animate,interval=1000)
    plt.tight_layout()

    plt.show()



