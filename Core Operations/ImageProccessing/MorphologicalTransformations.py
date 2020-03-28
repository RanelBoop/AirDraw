import  cv2
import numpy as np

img=cv2.imread('j.png',0)

kernel = np.ones((5,5),np.uint8)

#Erosion:
#So what happends is that, all the pixels near boundary will be discarded depending upon the size of kernel
erosion = cv2.erode(img,kernel,iterations = 1)

#Dilation:
# increases the white region in the image or size of foreground object increases.
dilation=cv2.dilate(img,kernel,iterations=1)

#Opening:
#erosion followed by dialation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#Closing:
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#Morphological Gradient:
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

