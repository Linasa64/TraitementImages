from skimage import io
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from random import randint, random
import numpy as np
import math as m


img = io.imread("./img/image2_reference.png")


# ALGO SALT AND PEPPER

for line in range(len(img)):
    for col in range(len(img)):
        if (randint(1, 10) == 1):
            if (random() <0.5):
                img[line, col] = 0
            else:
                img[line, col] = 255

#CALCUL SNR

from math import log

imgRef = io.imread("./img/image2_reference.png")
imgBruit = img


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
        

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 300))
axes[0].imshow(imgRef, cmap=cm.gray)
axes[0].set_title('Originale')
axes[1].imshow(imgBruit, cmap=cm.gray)
axes[1].set_title('Bruitée Salt&Pepper')
plt.text(3, 3, "BRUITAGE SALT&PEPPER - DEBRUITAGE CONVOLUTION\n", dict(color='red', x=-375, y=-70))
monsnr1 = snr(imgRef, imgBruit)
plt.text(3, 3, "SNR1 = " + str(monsnr1), dict(color='black', x=-300, y=-40))


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

nbPixels = 2
filtreConvolution(img, nbPixels)

# #Affichage

axes[2].imshow(img, cmap=cm.gray)
axes[2].set_title('Débruitée convolution')
monsnr2 = snr(imgRef, img)
plt.text(3, 3, "SNR2 = " + str(monsnr2), dict(color='black', x=20, y=-40))
plt.text(3, 3, "SNR1/SNR2 = " + str(100*(monsnr1/monsnr2)) + " %", dict(color='blue', x=-640, y=-40))


io.show   