import matplotlib.cm as cm
from skimage import io
import matplotlib.pyplot as plt



img = io.imread("./img/image1_bruitee_snr_10.8656.png")

##### DEFINITION DES FONCTIONS #####

def debruitageMoyenne(img):
    for line in range(1, (len(img)-1)):
        for col in range(1, len(img)-1):
            img[line, col] = moyenne_pixels(line, col)
     
            
def debruitageMediane(img):
    for line in range(1, (len(img)-1)):
        for col in range(1, len(img)-1):
            img[line, col] = mediane_pixels(line, col)
            

def moyenne_pixels(x, y):
    sum = 0
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)):
            sum = sum + int(img[line, col])
    sum = sum - int(img[x, y])
    res = sum/8
    return res


def mediane_pixels(x, y):
    liste = []
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)):
            liste.append(int(img[line, col]))
    liste.sort()
    return liste[4]
          

##### CHOIX DE LA METHODE #####

# debruitageMoyenne(img)
# choix = "MOYENNE"

debruitageMediane(img)
choix = "MEDIANE"


##### CALCUL SNR #####

from math import log

imgRef = io.imread("./img/image1_reference.png")
imgBruit = img

pSignal = 0
pBruit = 0

for line in range(0, len(imgBruit)):
    for col in range(0, len(imgBruit)):
        pSignal = pSignal + int(imgRef[line, col])**2
        pBruit = pBruit + (int(imgBruit[line, col])-int(imgRef[line, col]))**2
 

snr = 10*log((pSignal/pBruit), 10)
print("SNR: ", snr)

##### AFFICHAGE #####

img = io.imread("./img/image1_bruitee_snr_10.8656.png")
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 300))
axes[0].imshow(img, cmap=cm.gray)
axes[0].set_title('Bruitée')
axes[1].imshow(imgBruit, cmap=cm.gray)
axes[1].set_title('Débruitée')
axes[2].imshow(imgRef, cmap=cm.gray)
axes[2].set_title('Originale')
plt.text(3, 3, "DEBRUITAGE " + choix + "\n", dict(color='red', x=-500, y=-80))
plt.text(3, 3, "SNR = " + str(snr), dict(color='black', x=-550, y=-80))

io.show   