from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import filters

im = np.asarray(Image.open('..\\bookdata\\empire.jpg').convert('L'))

#Sobel derivative filters
imx = np.zeros(im.shape)
filters.sobel(im,1,imx)
imy = np.zeros(im.shape)
filters.sobel(im,0,imy)
magnitude = np.sqrt(imx**2+imy**2)

plt.gray()
plt.figure()
plt.imshow(im)
plt.figure()
plt.imshow(imx)
plt.figure()
plt.imshow(imy)
plt.figure()
plt.imshow(magnitude)
plt.show()
