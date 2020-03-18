import cv2
import IPython

img=cv2.imread('C:\\Users\\USER\\Desktop\\AirDraw\\SpongeImg\\Nature.jpg')

#cv2.getTickCount() returns the number of clock cycles
#cv2.getTickFrequency translates it to ms

#example
e1 = cv2.getTickCount()
for i in range(5,49,2):
    img = cv2.medianBlur(img,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print (t)
# Result I got is 0.521107655 seconds

#Optimization: On/Off
# check if optimization is enabled
print(cv2.useOptimized())

# time it res = cv2.medianBlur(img,49)
#10 loops, best of 3: 34.9 ms per loop

# Disable it
cv2.setUseOptimized(False)

print(cv2.useOptimized())

#%timeit res = cv2.medianBlur(img,49)
#10 loops, best of 3: 64.1 ms per loop


#Measuring Performance in IPython with %timeit method,see documentation

#Python and cv2 methods are usually faster than np methods when it comes to small operations.

#1.Avoid using loops in Python as far as possible, especially double/triple loops etc. They are inherently slow.
#2.Vectorize the algorithm/code to the maximum possible extent because Numpy and OpenCV are optimized for vector operations.
#3.Exploit the cache coherence.
#4.ever make copies of array unless it is needed. Try to use views instead. Array copying is a costly operation.



