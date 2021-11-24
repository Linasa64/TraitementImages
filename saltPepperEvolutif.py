# -*- coding: utf-8 -*-

from skimage import io
from random import randint, random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from math import log


img = io.imread("./img/image2_reference.png")

# ALGO SALT AND PEPPER

def saltPepper(img, x):
    for line in range(len(img)):
        for col in range(len(img)):
            if (randint(1, x) == 1):
                if (random() <0.5):
                    img[line, col] = 0
                else:
                    img[line, col] = 255

#CALCUL SNR

def snr(pImg, pImgRef):
    
    imgRef = pImgRef
    imgBruit = pImg

    pSignal = 0
    pBruit = 0
    
    for line in range(0, len(imgBruit)):
        for col in range(0, len(imgBruit)):
            pSignal = pSignal + int(imgRef[line, col])**2
            pBruit = pBruit + (int(imgBruit[line, col])-int(imgRef[line, col]))**2
     
    
    snr = 10*log((pSignal/pBruit), 10)
    print("SNR: ", snr)
    return snr

def g(x):
    img = io.imread("./img/image2_reference.png")
    saltPepper(img, x)
    return snr(img, io.imread("./img/image2_reference.png"))

       
def graphe(f,a,b,N):
    #trace le graphe de la fonction f entre a et b avec N segments
    lx = [a+i*(b-a)/N for i in range(N+1)]
    ly = [f(x) for x in lx]
    plt.plot(lx,ly)
    plt.xlabel("Valeur du paramètre x")
    plt.ylabel("SNR")
    plt.title("Bruit Sel et Poivre : Evolution du SNR en fonction du paramètre x")
    plt.show()  # affichage
       
# programme principal
graphe(g, 5, 105, 10)