import cv2
import numpy as np


img0=cv2.imread('C:\\Users\\USER\\Desktop\\AirDraw\\SpongeImg\\hand3.jpeg',0)
img=cv2.resize(img0,(400,400))
thresh=cv2.Canny(img,150,500)
#contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours,hierarchy=cv2.findContours(thresh,1,2)
print(contours)
#Moments:moments are used to calculate features like center of mass of object,are of obj ect.
cnt=contours[3]
M=cv2.moments(cnt)#gives dictionary of all moment values calculated
print(M)

#Centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

#Area
area = cv2.contourArea(cnt)
print(area)

#Perimiter:or arc length.second argument is to specify if contour is a closed shape or just an arc
perimeter = cv2.arcLength(cnt,False)

#Contour approximation:approximates a contour shape to another shape with less number of vertices.
#second argument is called epsilon, which is maximum distance from contour to approximated contour.
# It is an accuracy parameter.
#A wise selection of epsilon is needed to get the correct output.
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

#Convex Hull
hull=cv2.convexHull(cnt)
print(hull)

#Bounding Rectangle
x,y,w,h=cv2.boundingRect(cnt)
img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('handwin',img)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()

