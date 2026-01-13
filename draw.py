import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank',blank)

# blank[400:300, 300:400] = 0, 255, 0
# cv.imshow('Green',blank)

# drawing a rectangle
# cv.rectangle(blank, (0,0),(350,100),(250,0,250), thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)

# draw circle
# cv.circle(blank,(250,250),40,(0,0,255), thickness=5)
# cv.imshow('circle', blank)

# draw a line
# cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,255),thickness=2)
# cv.imshow('line',blank)

#write a text
cv.putText(blank, 'Hello Im sims',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.2,(0.255,255), thickness=3)
cv.imshow('text',blank)
cv.waitKey(0)