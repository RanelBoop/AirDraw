#To list all available mouse events run following code:
import cv2
import numpy as np
#events=[i for i in dir (cv2)if 'EVENT'in i]
#print events

#Draws circle whem mouse is clicked/mouse callback function
def draw_circle(event,x,y,flags,param):
    if event ==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

#create a black image
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()