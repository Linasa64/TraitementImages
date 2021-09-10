# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:43:15 2021

@author: linab
"""

import cv2 as cv

matrice = cv.imread("image2_reference.png")
print(matrice.shape)
print(matrice[0,0])