import cv2 as cv
import numpy as np
 
cap = cv.VideoCapture(0)
 
while(1):
 
    # Take each frame
    _, frame = cap.read()
 
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 
    # define range of blue color in HSV
    lower_red = np.array([0,50,150])
    upper_red = np.array([10,255,255])

    lower_blue = np.array([90, 140, 50])
    upper_blue = np.array([130,255, 255])

    lower_green = np.array([36, 50, 50])
    upper_green = np.array([85, 250, 255])
 
    # Threshold the HSV image to get only blue colors
    mask1 = cv.inRange(hsv, lower_red, upper_red)
    mask2 = cv.inRange(hsv, lower_blue,upper_blue )
    mask3 = cv.inRange(hsv, lower_green, upper_green) 

    mask = mask1 | mask2 | mask3
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
 
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv.destroyAllWindows()