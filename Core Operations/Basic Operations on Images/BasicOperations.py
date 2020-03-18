import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('C:\\Users\\USER\\Desktop\\AirDraw\\SpongeImg\\Nature.jpg')#instances of letters like \U and \N can
#be mistaken for unicode escapes.to avoid it we can put an r before the string to make it raw,or put double slashes

#accessing pixels
px=img[100,100]#row and collumn coordinates
print (px)#for BGR image it returns an array of [Blue Green Red] values.for grayscale just corresponding intensity is returned

#accessing only blue pixel
blue=img[100,100,0]
print (blue)
#we can modify their values the same way
img[100,100]=[255,255,255]
print (img[100,100])

#better pixel accessing method:

# accessing RED value
img.item(10,10,2)


# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

#accessing image shape.function returns a tuple of number of rows,columns,and channels(if image is in color)
#also a great way to check if the image is color or grayscale
print(img.size)

#image dataType,img.dtype is very important while debugging because a large number of errors in OpenCV-Python code
# is caused by invalid datatype.
print(img.dtype)

#Image ROI(region of image)
hat=img[280:340, 330:390]#cloning and moving a part of the picture
img[273:333, 100:160]=hat

#Splitting and merging image channels
b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))
#or
b = img[:,:,0]
#make all red pixels zero using nympy indexing
img[:,:,2] = 0

#making a border for images
img1 = cv2.imread('C:\\Users\\USER\\Desktop\\AirDraw\\SpongeImg\\opencv_logo.png')

BLUE=[255,0,0]

replicate = cv2.copyMakeBorder(img1,80,80,80,80,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,80,80,80,80,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,80,80,80,80,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,80,80,80,80,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,80,80,80,80,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL'),plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE'),plt.xticks([]),plt.yticks([])
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT'),plt.xticks([]),plt.yticks([])
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101'),plt.xticks([]),plt.yticks([])
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP'),plt.xticks([]),plt.yticks([])
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT'),plt.xticks([]),plt.yticks([])


plt.show()