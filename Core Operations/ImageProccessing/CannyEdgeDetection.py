import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('C:\\Users\\USER\\Desktop\\AirDraw\\SpongeImg\\hand3.jpeg',0)
edges=cv2.Canny(img,100,100)
img_resized=cv2.resize(img,(300,300))


_minVal=0
_maxVal=0
windowTrack=cv2.namedWindow('tracker')

#windowTrack1=cv2.namedWindow('tracker1')

def on_trackbarMin(val):
    _minVal=val
    edges = cv2.Canny(img_resized,_minVal,_maxVal)
    cv2.imshow(windowTrack,edges)


def on_trackbarMax(val):
    _maxVal=val
    edges = cv2.Canny(img_resized,_minVal,_maxVal)
    cv2.imshow(windowTrack,edges)

cv2.createTrackbar('maxValTrack','tracker',100,1000,on_trackbarMax)
cv2.createTrackbar('minValTrack','tracker',100,1000,on_trackbarMin)


plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('originalImage'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('EdgeImage'),plt.xticks([]),plt.yticks([])
plt.show()