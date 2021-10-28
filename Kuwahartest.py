import matplotlib.cm as cm
from skimage import io
import matplotlib.pyplot as plt
import math
import statistics
import numpy as np

#Affichage

img = io.imread("image1_bruitee_snr_10.8656.png")
       
       

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
imgRefBruit = io.imread("image1_bruitee_snr_10.8656.png")
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 300))
axes[0].imshow(imgRefBruit, cmap=cm.gray)
axes[0].set_title('Bruitée')
axes[1].imshow(img, cmap=cm.gray)
axes[1].set_title('Débruitée')
axes[2].imshow(imgRef, cmap=cm.gray)
axes[2].set_title('Originale')

io.show   