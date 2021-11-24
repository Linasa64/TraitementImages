# -*- coding: utf-8 -*-

import matplotlib.cm as cm
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import math as m
from pylab import *
from math import log



img = io.imread("./img/image1_bruitee_snr_10.8656.png")

##### DEFINITION DES FONCTIONS #####


## Applique le filtre par convolution à l'image
def filtreConvolution(img, nbPixelsCoté):
    filtreGauss = convoGauss(nbPixelsCoté)
    sum=0
    for line in range(nbPixelsCoté, len(img)-nbPixelsCoté):
        for col in range(nbPixelsCoté, len(img)-nbPixelsCoté):
                ptm = pixelToMatrice(line, col, nbPixelsCoté)
                ptmGauss = ptm*filtreGauss
                #afficherCarre(ptmGauss, nbPixelsCoté)
                for line2 in range(0, nbPixelsCoté*2+1):
                    for col2 in range(0, nbPixelsCoté*2+1):
                        sum = sum + ptmGauss[line2][col2]
                img[line, col] = sum
                sum=0

## Fonction permettant d'afficher l'environnement d'un pixel [DEBUGGAGE]
def afficherCarre(mat, nbPixelsCoté):
    for line in range((0), (nbPixelsCoté*2+1)):
        print(" ")
        for col in range((0), (nbPixelsCoté*2+1)):
            print(img[line, col], end=" ")
    print ("\n\n")
    
## Renvoie une matrice des pixels environnant un pixel donné
def pixelToMatrice(x, y, nbPixelsCoté):
    entourage = np.zeros((2*nbPixelsCoté+1, 2*nbPixelsCoté+1))
    indX = x-nbPixelsCoté
    indY = y-nbPixelsCoté
    matX = 0
    matY = 0
    
    while(indX<=x+nbPixelsCoté):
        while(indY<=y+nbPixelsCoté):
            entourage[matX][matY] = img[indX, indY]
            indY+=1
            matY+=1
        indX+=1
        matX+=1
        indY=y-nbPixelsCoté
        matY=0
    return entourage
      
## Renvoie la matrice de connvolution correspondant au nbre de pixels environnants donnés      
def convoGauss(nbPixelsCoté):
    sigma = 0.5 #importance des pixels sur le côté par rapport à celui central
    h = np.zeros((2*nbPixelsCoté+1, 2*nbPixelsCoté+1))
    somme = 0
    for line in range(-nbPixelsCoté, nbPixelsCoté+1) :
        for col in range(-nbPixelsCoté, nbPixelsCoté+1) :
            h[line][col] = (1/(2*m.pi*sigma**2))*m.exp(-(col**2+line**2)/2*(sigma**2))
            somme += h[line][col]
    h = h/somme
    return h


##### CALCUL SNR #####

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



img = io.imread("./img/image1_bruitee_snr_10.8656.png")
filtreConvolution(img, 1)
snr1=snr(img, io.imread("./img/image1_reference.png"))
img = io.imread("./img/image1_bruitee_snr_10.8656.png")
filtreConvolution(img, 2)
snr2=snr(img, io.imread("./img/image1_reference.png"))
img = io.imread("./img/image1_bruitee_snr_10.8656.png")
filtreConvolution(img, 3)
snr3=snr(img, io.imread("./img/image1_reference.png"))
img = io.imread("./img/image1_bruitee_snr_10.8656.png")
filtreConvolution(img, 4)
snr4=snr(img, io.imread("./img/image1_reference.png"))
img = io.imread("./img/image1_bruitee_snr_10.8656.png")
filtreConvolution(img, 5)
snr5=snr(img, io.imread("./img/image1_reference.png"))


x = array([1, 2, 3, 4, 5])
y = array([snr1, snr2, snr3, snr4, snr5])
plt.xlabel("Nombre de pixels environnants")
plt.ylabel("SNR")
plot(x, y)

show()
