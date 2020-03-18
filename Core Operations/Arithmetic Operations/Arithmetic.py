import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('C:\\Users\\USER\\Desktop\\AirDraw\\SpongeImg\\twitter_logo.png')
#images must be same size
img2=cv2.imread('C:\\Users\\USER\\Desktop\\AirDraw\\SpongeImg\\facebook_logo.png')

dst=cv2.addWeighted(img1,0.7,img2,0.3,0)#see formula in documentation

cv2.imshow('windowName',dst)

cv2.waitKey(0)#any key
cv2.destroyAllWindows()

#Bitwise operations

img=cv2.imread('C:\\Users\\USER\\Desktop\\AirDraw\\SpongeImg\\Nature.jpg')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels=img1.shape
roi=img[0:rows,0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

cv2.imshow('f',img2gray),cv2.waitKey(0),cv2.destroyAllWindows()

ret,mask=cv2.threshold(img2gray,250,255,cv2.THRESH_BINARY)#threshold of values of gray between 0 and 255
mask_inv=cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('f',img_bg),cv2.waitKey(0),cv2.destroyAllWindows()

# Take only region of logo from logo image.
img1_fg = cv2.bitwise_and(img1,img1,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img_bg,img1_fg)
img[0:rows, 0:cols ] = dst

cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()