# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:03:17 2021

@author: aubin
"""

from skimage import io

# on importe l'image et on le transforme en tableau numpy
img = io.imread("image2_reference.png")

for i in range (img.shape[0]):
    
    img[i,] = 0

# afficher l'image
io.imshow(img)
io.show
