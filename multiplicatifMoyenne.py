from skimage import io
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from random import randint
import numpy as np
import math as m


img = io.imread("./img/image2_reference.png")


# ALGO BRUIT MULTIPLICATIF
for line in range(len(img)):
    for col in range(len(img)):
        x = randint(0, 100)-50
        x/=10
        if (randint(1, 10) == 1):
            if (img[line, col] *(x)<0):
                img[line, col] = 0
            elif(img[line, col] *(x)>255):
                img[line, col] = 255
            else:
                img[line, col] = img[line, col] * (x)


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
axes[1].set_title('Bruitée multiplicatif')
plt.text(3, 3, "BRUITAGE MULTIPLICATIF - DEBRUITAGE MEDIANE\n", dict(color='red', x=-375, y=-70))
monsnr1 = snr(imgRef, imgBruit)
plt.text(3, 3, "SNR = " + str(monsnr1), dict(color='black', x=-300, y=-40))


def debruitageMoyenne(img):
    for line in range(1, (len(img)-1)):
        for col in range(1, len(img)-1):
            img[line, col] = moyenne_pixels(line, col)
     
            
def debruitageMediane(img):
    for line in range(1, (len(img)-1)):
        for col in range(1, len(img)-1):
            img[line, col] = mediane_pixels(line, col)
            

def moyenne_pixels(x, y):
    sum = 0
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)):
            sum = sum + int(img[line, col])
    sum = sum - int(img[x, y])
    res = sum/8
    return res


def mediane_pixels(x, y):
    liste = []
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)):
            liste.append(int(img[line, col]))
    liste.sort()
    return liste[4]
          

##### CHOIX DE LA METHODE #####

# debruitageMoyenne(img)
# choix = "MOYENNE"

debruitageMediane(img)
choix = "MEDIANE"

# #Affichage

axes[2].imshow(img, cmap=cm.gray)
axes[2].set_title('Débruitée Médiane')
monsnr2 = snr(imgRef, img)
plt.text(3, 3, "SNR = " + str(monsnr2), dict(color='black', x=20, y=-40))
plt.text(3, 3, "SNR1/SNR2 = " + str(100*(monsnr1/monsnr2)) + " %", dict(color='blue', x=-640, y=-40))


io.show   