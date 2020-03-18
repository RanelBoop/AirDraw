import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('SpongeImg\SpongebobMeme.png',0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])#hides tick values
plt.show()
'''
cv2.namedWindow('windowName',cv2.WINDOW_NORMAL)
cv2.imshow('windowName',img)
KEY=cv2.waitKey(0)
if KEY==ord('s'):
    cv2.imwrite('spongeGray.png',img)
else:
    cv2.destroyAllWindows()
'''


