from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import filters

im = np.asarray(Image.open('..\\bookdata\\empire.jpg'))
g = np.zeros(im.shape)
for i in range(3):
    g[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
#g = np.uint8(g)
n = 255.0 * im / g

print(im[100][100], g[100][100], n[100][100])

plt.figure()
plt.imshow(im)
plt.figure()
plt.imshow(n)

#plt.show()
