# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:04:00 2021

@author: aubin
"""

import numpy as np
from skimage import io

img = io.imread("image1_bruitee_snr_10.8656.png")

def filtreRehausseur(img):
    rehausseur = ([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

    for line in range(0, len(img)):
        for col in range(0, len(img)):
                sum = 0
                for line2 in range(0, 3):
                    for col2 in range(0, 3):
                        ptm = pixelToMatrice(line2, col2)
                        sum += ptm[line2, col2]*rehausseur[line2, col2]
                img[line, col] = sum

def pixelToMatrice(x, y):
    entourage = np.array([[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]])
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)):
            entourage[line, col] = img[line, col]
    return entourage
            
#Affichage
filtreRehausseur(img)
io.imshow(img)
io.show