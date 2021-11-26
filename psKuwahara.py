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
plt.text(3, 3, "BRUITAGE SALT&PEPPER - DEBRUITAGE KUWAHARA\n", dict(color='red', x=-375, y=-70))
monsnr1 = snr(imgRef, imgBruit)
plt.text(3, 3, "SNR1 = " + str(monsnr1), dict(color='black', x=-300, y=-40))


## Choisit la moyenne de la zone avec l'écart-type le plus bas
def moyenneEnFonctionEcartTypeMin(a, b, c, d):
    listeEcartsTypes = [np.nanstd(a), np.nanstd(b), np.nanstd(c), np.nanstd(d)]
    posMin = listeEcartsTypes.index(min(listeEcartsTypes))
    
    if(posMin == 0):
        return a.mean()
    elif (posMin == 1):
        return b.mean()
    elif (posMin == 2):
        return c.mean()
    else:
        return d.mean()
     
## Crée les matrices correspondant à chacune des 4 zones pour chaque pixel
## Affecte au pixel courant la moyenne de la zone avec l'écart-type le plus bas
for line in range(2, len(img)-2) :
   for col in range(2, len(img)-2) :
            
       a = np.array([[img[line-2, col-2], img[line-2, col-1], img[line-2, col]],
             [img[line-1, col-2], img[line-1, col-1], img[line-1, col]], 
             [img[line, col-2], img[line, col-1], img[line, col]]])
            
       b = np.array([[img[line-2, col+2], img[line-2, col+1], img[line-2, col]],
             [img[line-1, col+2], img[line-1, col+1], img[line-1, col]],
             [img[line, col+2], img[line, col+1], img[line, col]]])
            
       c = np.array([[img[line, col-2], img[line, col-1], img[line, col]],
            [img[line+1, col-2], img[line+1, col-1], img[line+1, col]],
            [img[line+2, col-2], img[line+2, col-1], img[line+2, col]]])
            
       d = np.array([[img[line, col+2], img[line, col+1], img[line, col]],
            [img[line+1, col+2], img[line+1, col+1], img[line+1, col]],
            [img[line+2, col+2], img[line+2, col+1], img[line+2, col]]])
       
       img[line, col] = moyenneEnFonctionEcartTypeMin(a, b, c, d)

# #Affichage

axes[2].imshow(img, cmap=cm.gray)
axes[2].set_title('Débruitée Kuwahara')
monsnr2 = snr(imgRef, img)
plt.text(3, 3, "SNR2 = " + str(monsnr2), dict(color='black', x=20, y=-40))
plt.text(3, 3, "SNR1/SNR2 = " + str(100*(monsnr1/monsnr2)) + " %", dict(color='blue', x=-640, y=-40))


io.show   