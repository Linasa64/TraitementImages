# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:43:15 2021

@author: linab
"""

#pip install opencv-python pour que ça marche la première fois

# import cv2 as cv

# matrice = cv.imread("image2_reference.png")
# print(matrice.shape)
# print(matrice[0,0])

# matG = cv.cvtColor(matrice, cv.COLOR_BGR2GRAY)
# print(matG.shape)
# print(matG[0,0])

# matG = cv.imread("image2_reference.png")
# cv.imwrite("resultat.jpg", matG)

# cv.imshow("Image de matG", matG)
# cv.waitKey(0)
# cv.destroyAllWindows()

from skimage import io

img = io.imread("image2_reference.png")

print (img.shape)
print (img[0,0])

for i in range(0,img.shape[0]):
    img[i,100] = 255
    
io.imshow(img)
io.show