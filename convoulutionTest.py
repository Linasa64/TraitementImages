# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:04:00 2021

@author: aubin
"""

import matplotlib.cm as cm
import numpy as np
from skimage import io
import matplotlib.pyplot as plt


img = io.imread("image1_bruitee_snr_10.8656.png")

def filtreRehausseur(img):
    rehausseurM = ([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])
    
    # rehausseurGaussien = ([[1/16, 1/8, 1/16],
    #                        [1/8, 1/4, 1/8],
    #                        [1/16, 1/8, 1/16]])
    
    # rehausseurEdgeDetector = ([[-1, -1, -1],
    #                            [-1, 8, -1],
    #                            [-1, -1, -1]])

    for line in range(1, len(img)-1):
        for col in range(1, len(img)-1):
                sum = 0
                for line2 in range(0, 3):
                    for col2 in range(0, 3):
                        #print("line : ", line, " / col : ", col)
                        ptm = pixelToMatrice(line, col)
                        sum += ptm[line2][col2]*rehausseurM[line2][col2]
                img[line, col] = sum

def pixelToMatrice(x, y):
    entourage = np.array([[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]])
    indX = x-1
    indY = y-1
    matX = 0
    matY = 0
    
    while(indX<=x+1):
        while(indY<=y+1):
            #print("indX :", indX, " / indY :", indY, " / matX: ", matX, " / matY :", matY)
            entourage[matX][matY] = img[indX, indY]
            indY+=1
            matY+=1
        indX+=1
        matX+=1
        indY=y-1
        matY=0
    return entourage
            



filtreRehausseur(img)


## CALCUL SNR

from math import log, log10

imgRef = io.imread("image1_reference.png")
imgBruit = img

pSignal = 0
pBruit = 0

for line in range(0, len(imgBruit)):
    for col in range(0, len(imgBruit)):
        pSignal = pSignal + int(imgRef[line, col])**2
        pBruit = pBruit + (int(imgBruit[line, col])-int(imgRef[line, col]))**2
 

print("pSignal : ", pSignal)
print("pBruit : ", pBruit)
snr = 10*log((pSignal/pBruit), 10)
print("SNR: ", snr)

#Affichage
# io.imshow(img)
img = io.imread("image1_bruitee_snr_10.8656.png")
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 300))
axes[0].imshow(img, cmap=cm.gray)
axes[0].set_title('Bruitée')
axes[1].imshow(imgBruit, cmap=cm.gray)
axes[1].set_title('Débruitée')
axes[2].imshow(imgRef, cmap=cm.gray)
axes[2].set_title('Originale')

io.show   



#Affichage


imgRef = io.imread("image1_reference.png")
imgBruit = io.imread("image1_bruitee_snr_10.8656.png")
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 300))
axes[0].imshow(imgBruit, cmap=cm.gray)
axes[0].set_title('Bruitée')
axes[1].imshow(img, cmap=cm.gray)
axes[1].set_title('Débruitée')
axes[2].imshow(imgRef, cmap=cm.gray)
axes[2].set_title('Originale')

io.show   