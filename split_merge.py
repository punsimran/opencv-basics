import cv2 as cv
import numpy as np

img = cv.imread('photos/nature.png')

b,g,r = cv.split(img)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow('red',r)
cv.waitKey(0)