import numpy as np
from matplotlib import pyplot as plt
import cv2

#-1 in the end makes the shape
#fill in itself,other numbers will represent a thickness in pixels

#Drawing a line
img=np.zeros((512,512,3),np.uint8)
line=cv2.line(img,(0,0),(511,511),(255,0,0),5)

#Drawing a rectangle
rect=cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#Drawing a circle
circ=cv2.circle(img,(447,63),63,(0,0,255),-1)

#Drawing an ellipse
elli=cv2.ellipse(img,(256,256),(100,50),0,0,360,255,3)

#Drawing a polygon
pts=np.array([[10,5],[20,30],[70,20],[20,50]],np.int32)
pts=pts.reshape((-1,1,2))
poly=cv2.polylines(img,[pts],True,(0,255,0))

#Drawing text
font=cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

plt.imshow(img,interpolation='bicubic')
plt.show()