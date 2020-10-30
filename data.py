from itertools import count
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def graph():
    house = np.random.normal(200000,20000,2000)
    plt.hist(house,200)
    plt.show()

while True:

    pullData = open("data.txt","r").read()

    dataList = pullData.split('\n')

    data = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    x_index = []

    index = count()
    plt.style.use('fivethirtyeight')

    def animate(i):
        x_index.append(next(index))
        a = open('data.txt','r').read()
        lineas = a.split('\n')

        #Settings of graph
        plt.style.use('fivethirtyeight')
        plt.cla()
        plt.ylabel("Percentage of traffic")
        plt.ylim((0,100))
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







        plt.legend(loc='upper left')
        plt.tight_layout()


    ani = FuncAnimation(plt.gcf(),animate,interval=1000)
    plt.tight_layout()

    plt.show()



