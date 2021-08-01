from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import filters

im = np.asarray(Image.open('..\\bookdata\\empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im, 2)
un = im - im2

im = np.asarray(Image.open('..\\bookdata\\empire.jpg'))
im2 = filters.gaussian_filter(im, 2)
un2 = np.uint8(im *0.9 + (im - im2) * 0.1)
print(un2.shape, un2.dtype, un2.min(), un2.max())

plt.figure()
plt.imshow(im)
plt.figure()
plt.imshow(un2)

#plt.figure()
#plt.gray()
#plt.imshow(un)

plt.show()
