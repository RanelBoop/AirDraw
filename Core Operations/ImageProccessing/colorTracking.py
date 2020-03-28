import  cv2
import numpy as np

cap=cv2.VideoCapture(0)

while(True):
    _,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #define kernel for gap closing in mask
    kernel = np.ones((5, 5), np.uint8)


    #define range of blue in hsv
    lower_blue=np.array([160,80,1])
    upper_blue=np.array([255,255,160])

    # threshold of only blue colors
    mask=cv2.inRange(frame,lower_blue,upper_blue)

    # bitwise add:adds the selected mask to selected images
    res=cv2.bitwise_and(frame,frame,mask=mask)

    #blur = cv2.bilateralFilter(res, 9, 75, 75) removes object texture
    #blur=cv2.GaussianBlur(res,(5,5),0) removes gaussian noise

    closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('closed', closing)
    cv2.imshow('result',res)


    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()