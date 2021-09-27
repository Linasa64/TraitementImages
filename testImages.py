# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:43:15 2021

@author: linab
"""

from skimage import io
from random import randint, random

img = io.imread("image2_reference.png")


# # ALGO SALT AND PEPPER
# for line in range(len(img)):
#     for col in range(len(img)):
#         if (randint(1, 10) == 1):
#             if (random() <0.5):
#                 img[line, col] = 0
#             else:
#                 img[line, col] = 255

# # ALGO BRUIT ADDITIF
# for line in range(len(img)):
#     for col in range(len(img)):
#         if (randint(1, 2) == 1):
#             r = randint(-100, 0)
#             if (img[line, col] + r < 0):
#               img[line, col] = 0
#             elif (img[line, col] + r > 255) :
#               img[line, col] = 255 
#             else :
#                 img[line, col] = img[line, col] + r


                
# # ALGO BRUIT MULTIPLICATIF
# for line in range(len(img)):
#     for col in range(len(img)):
#         if (randint(1, 3) == 1):
#             if (img[line, col] * (1-1.5)<0):
#                 img[line, col] = 0
#             else :
#                 img[line, col] = img[line, col] * (1-1.5)
    


#CALCUL SNR

from math import log, log10

imgRef = io.imread("image1_reference.png")
imgBruit = io.imread("image1_bruitee_snr_10.8656.png")

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


# #Affichage
# io.imshow(img)
# io.show