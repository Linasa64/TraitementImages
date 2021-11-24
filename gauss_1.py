from skimage import io, color
import numpy as np
import matplotlib.pyplot as plt

image = io.imread('./img/image1_bruitee_snr_10.8656.png')
grey_image = color.rgb2gray(np.array(image))
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20,10))
# Image en nuance de gris
axs[0].imshow( grey_image, cmap = 'Greys_r')
axs[0].set_title( 'Image originelle' )

grey_image2=grey_image


def gauss(taille_filtre):
    
    filtre = np.zeros((2*taille_filtre+1,2*taille_filtre+1))
    sigma = 0.5
    somme = 0

    for x in range(-taille_filtre,taille_filtre+1):
        for y in range(-taille_filtre,taille_filtre+1):
            filtre[x][y] = ((1/(2*np.pi*sigma**2))*np.exp(-(x**2+y**2)/2*(sigma**2)))
            somme += filtre[x][y]
    filtre=filtre/somme
    
    return filtre

def conv3x3(grey_image):
    grey_image2 = grey_image
    zeb=gauss(2)
    taille_matrice = (5,5)
    filtre_convolution = np.ones(taille_matrice)
    # Parcours des lignes de pixels
    for ligne in range(grey_image.shape[0]-4):
        # Parcours des colones de pixels
        for colonne in range(grey_image.shape[1]-4):
            for x in range(filtre_convolution.shape[0]):
                for y in range(filtre_convolution.shape[1]):
                    filtre_convolution[x][y] = grey_image[ligne+x][colonne+y]*zeb[x][y]
            filtre_convolution[2][2] = (sum(sum(filtre_convolution)))
            grey_image2[ligne][colonne]=filtre_convolution[2][2]
    return grey_image2


                
axs[1].imshow(conv3x3(grey_image2), cmap = 'Greys_r')
axs[1].set_title( 'Image filtre' )

#CALCUL SNR

from math import log

imgRef = io.imread('./img/image1_bruitee_snr_10.8656.png')
imgBruit = grey_image2


pSignal = 0
pBruit = 0

for line in range(0, len(imgBruit)):
    for col in range(0, len(imgBruit)):
        pSignal = pSignal + int(imgRef[line, col])**2
        pBruit = pBruit + (int(imgBruit[line, col])-int(imgRef[line, col]))**2
        

snr = 10*log((pSignal/pBruit), 10)
print("SNR: ", snr)                