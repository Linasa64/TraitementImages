# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:03:17 2021

@author: aubin
"""
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
from skimage import io

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow("image2_reference.png")
ax.set_title('Img2Ref')

ax = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow("image1_reference.png")
ax.set_title('Img1Ref')