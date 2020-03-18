import numpy as np
import cv2

cap=cv2.VideoCapture(0)
#In some cases you may receive and error as result of the cap not being initialized
#The cap.read() method returns bool of wether the frame is read correctly or not
#You can see wether it's initialized or not by cap.isOpened()/otherwise use cap.Open()
#also cap has set of cap.get(propId) features.
#cap.get(3) and 4 gives the width and height of video.you can change by using:
#ret=cap.set(3,320) and ret=cap.set(4,240)

while(True):
    #capture frame by frame
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('vidFrameName',gray)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

