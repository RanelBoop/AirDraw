import cv2
from matplotlib import pyplot as plt
import numpy as np

img0=cv2.imread('C:\\Users\\USER\\Desktop\\AirDraw\\SpongeImg\\hand3.jpeg')
img=cv2.resize(img0,(400,400))
#Creating trackbars for canny edge detection
'''
_minVal=0
_maxVal=0
edges=cv2.Canny(img,100,100)
TrackerWindow=cv2.namedWindow('TrackerWin')

def OnTrackBarMin(val):
    _minVal=val
    edges=cv2.Canny(img,_minVal,_maxVal)
    cv2.imshow(TrackerWindow,edges)

def OnTrackBarMax(val):
    _maxVal=val
    edges=cv2.Canny(img,_minVal,_maxVal)
    cv2.imshow(TrackerWindow,edges)

cv2.createTrackbar('maxValTrack','TrackerWin',100,1000,OnTrackBarMax)
cv2.createTrackbar('minValTrack','TrackerWin',100,1000,OnTrackBarMin)

plt.subplot(121),plt.imshow(edges,cmap='gray')
plt.title('originalImage'),plt.xticks([]),plt.yticks([])
plt.show() 
'''
#Using regular thresholding to get the "edged" image:
#imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,thresh=cv2.threshold(imgray,127,255,0)

#Using Canny Edge Detection to get the "edged image":
#thresh=cv2.Canny(img,100,130)
thresh=cv2.Canny(img,150,500)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#thresh is
#only the name of the thresholded image

#print(contours)
img=cv2.drawContours(img,contours,-1,(0,255,0),3)

plt.imshow(img,cmap='gray')
plt.show()