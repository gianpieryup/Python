# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=25)
    plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.


if __name__=="__main__":
    plotear_temperaturas()