from numpy.random import *
import pylab
import matplotlib.pyplot as plt
from matplotlib.pyplot import *


p1 = (2*256+2*254)/256**2*100
p2 = (4*256+4*252)/256**2*100
p3 = (6*256+6*250)/256**2*100
p4 = (8*256+8*248)/256**2*100

print(p1)
print(p2)
print(p3)
print(p4)


x = ['1 pixel', '2 pixels', '3 pixels', '4 pixels']
h = [p1, p2, p3, p4]
width = 0.2

res = bar(x, h, width, color='gray')
pylab.xticks(x, x, rotation=0)
plt.title('Pourcentage de pixels non traités en fonction de la taille des bordures')
xlabel("Nombre de pixels de la bordure")
ylabel("Total de pixels non traités (%)")

show()
