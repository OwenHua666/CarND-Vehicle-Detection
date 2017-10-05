import cv2
import matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
plt.interactive(False)
img = mpimg.imread('test_images/test1.jpg')
plt.figure()
plt.show(img)
print(img.shape)