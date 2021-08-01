from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import filters

im = np.asarray(Image.open('..\\bookdata\\empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im, 10)
im5 = filters.gaussian_filter(im, 20)
im9 = filters.gaussian_filter(im, 30)

plt.figure()
plt.gray()
plt.contour(im, origin='image')
plt.axis('equal')
plt.axis('off')

#plt.figure()
#plt.hist(im.flatten(), 128)
#plt.imshow(im)
plt.figure()
#plt.hist(im2.flatten(), 128)
plt.imshow(im2)
plt.figure()
#plt.hist(im5.flatten(), 128)
plt.imshow(im5)
plt.figure()
#plt.hist(im9.flatten(), 128)
plt.imshow(im9)
plt.show()
