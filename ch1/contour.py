from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
im = np.asarray(Image.open('..\\bookdata\\empire.jpg').convert('L'))

plt.figure()
plt.gray()
plt.contour(im, origin='image')
plt.axis('equal')
plt.axis('off')

plt.figure()
plt.hist(im.flatten(), 128)
plt.show()
