from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.geometry("1x1")
def graph():
    house = np.random.normal(200000,20000,2000)
    plt.hist(house,200)
    plt.show()

but = Button(root,command=graph())
but.pack()
root.mainloop()
