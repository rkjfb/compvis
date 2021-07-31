from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = np.asarray(Image.open('..\\bookdata\\empire.jpg'))

plt.imshow(im)
plt.show()
