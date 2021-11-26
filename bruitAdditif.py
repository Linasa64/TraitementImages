from skimage import io
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from random import randint


img = io.imread("./img/image2_reference.png")


# # ALGO BRUIT ADDITIF

for line in range(len(img)):
    for col in range(len(img)):
        if (randint(1, 2) == 1):
            r = randint(0, 100)-50
            if (img[line, col] + r < 0):
              img[line, col] = 0
            elif (img[line, col] + r > 255) :
              img[line, col] = 255 
            else :
                img[line, col] = img[line, col] + r


#CALCUL SNR

from math import log

imgRef = io.imread("./img/image2_reference.png")
imgBruit = img


pSignal = 0
pBruit = 0

for line in range(0, len(imgBruit)):
    for col in range(0, len(imgBruit)):
        pSignal = pSignal + int(imgRef[line, col])**2
        pBruit = pBruit + (int(imgBruit[line, col])-int(imgRef[line, col]))**2
        

snr = 10*log((pSignal/pBruit), 10)
print("SNR: ", snr)

# #Affichage

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 300))
axes[0].imshow(imgBruit, cmap=cm.gray)
axes[0].set_title('Bruitée')
axes[1].imshow(imgRef, cmap=cm.gray)
axes[1].set_title('Référence')
plt.text(3, 3, "BRUIT ADDITIF\n", dict(color='red', x=-65, y=-30))
plt.text(3, 3, "SNR = " + str(snr), dict(color='black', x=-100, y=-30))

io.show   