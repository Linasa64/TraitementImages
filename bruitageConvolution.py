import matplotlib.cm as cm
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import math as m


img = io.imread("image1_bruitee_snr_10.8656.png")

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


##### CALCUL SNR #####

from math import log

imgRef = io.imread("image1_reference.png")
imgBruit = img

pSignal = 0
pBruit = 0

for line in range(0, len(imgBruit)):
    for col in range(0, len(imgBruit)):
        pSignal = pSignal + int(imgRef[line, col])**2
        pBruit = pBruit + (int(imgBruit[line, col])-int(imgRef[line, col]))**2
 

snr = 10*log((pSignal/pBruit), 10)
print("SNR: ", snr)


##### AFFICHAGE #####

imgRefBruit = io.imread("image1_bruitee_snr_10.8656.png")
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 300))
axes[0].imshow(imgRefBruit, cmap=cm.gray)
axes[0].set_title('Bruitée')
axes[1].imshow(img, cmap=cm.gray)
axes[1].set_title('Débruitée')
axes[2].imshow(imgRef, cmap=cm.gray)
axes[2].set_title('Originale')
plt.text(3, 3, "DEBRUITAGE CONVOLUTION, " + str(nbPixels) + " PIXELS ENVIONNANTS\n", dict(color='red', x=-750, y=-80))
plt.text(3, 3, "SNR = " + str(snr), dict(color='black', x=-550, y=-80))

io.show