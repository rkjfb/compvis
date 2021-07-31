from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import filters

im = np.asarray(Image.open('..\\bookdata\\empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im, 5)

plt.gray()
plt.imshow(im2)
plt.show()
