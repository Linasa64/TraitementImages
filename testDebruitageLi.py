# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:57:09 2021

@author: linab
"""

import matplotlib.cm as cm
from skimage import io


img = io.imread("image1_bruitee_snr_10.8656.png")


def debruitage(img):
    for line in range(1, (len(img)-2)):
        for col in range(1, len(img)-2):
            img[line, col] = moyenne_pixels(line, col)


def moyenne_pixels(x, y):
    sum = 0
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)):
            sum = sum + int(img[line, col])
    res = sum - int(img[x, y])
    res = sum/8
    return res


def afficherCarrePixels(x, y):
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)): 
            print(img[line, col])

# print(moyenne_pixels(10, 10))
# afficherCarrePixels(10, 10)
debruitage(img)

#Affichage
# io.imshow(img)
io.imshow(img, cmap=cm.gray)
io.show   