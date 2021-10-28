import matplotlib.cm as cm
from skimage import io
import matplotlib.pyplot as plt
from PIL import Image

#Affichage

img = Image.open("squirrel.jpg")
imgKuwa = img

print()
print(img.size);

for line in range(0, 396) :
   for col in range(0, 500) :
            
       a = ([[img[line-2, col-2], img[line-2, col-1], img[line-2, col]],
             [img[line-1, col-2], img[line-1, col-1], img[line-1, col]], 
             [img[line, col-2], img[line, col-1], img[line, col]]])
            
       b = ([[img[line-2, col+2], img[line-2, col+1], img[line-2, col]],
             [img[line-1, col+2], img[line-1, col+1], img[line-1, col]],
             [img[line, col+2], img[line, col+1], img[line, col]]])
            
       c = ([[img[line, col-2], img[line, col-1], img[line, col]],
            [img[line+1, col-2], img[line+1, col-1], img[line+1, col]],
            [img[line+2, col-2], img[line+2, col-1], img[line+2, col]]])
            
       d = ([[img[line, col+2], img[line, col+1], img[line, col]],
            [img[line+1, col+2], img[line+1, col+1], img[line+1, col]],
            [img[line+2, col+2], img[line+2, col+1], img[line+2, col]]])

       a2 = a[0]+a[1]+a[2]; 
       
print(a2);
    
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 7))
axes[0].imshow(imgKuwa, cmap=cm.gray)
axes[0].set_title('Squirrrrrrrel')
axes[1].imshow(img, cmap=cm.gray)
axes[1].set_title('Kuwahara')

io.show 
