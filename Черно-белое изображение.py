from PIL import Image
import numpy as np


image = np.asarray(Image.open('images/image.jpg'))
Image.fromarray(np.uint8(image(C = 0.2989 * R + 0.5870 * G + 0.1140 * B))).save('res.jpg')
