# MORPHOLOGICAL TRANSFORMATION
# perform on binary image
# operators: erosion & dilation

# 1. EROSION:
# it enrodes away the boundaries of foreground object(Always try to keep foreground in white)
# a pixel in the orginal img: 0 or 1 will be considered 1 only if all the pixels under kernel 1. otherwise eroded made to zero.
# all the pixels near boundary will be discarded depending upon the size of kernel.
# the size of the foreground object decreases or simply white region decreases in the img.
# used to remove the small white noises, detach connected objects.
# 

import cv2 as cv
import numpy as np
 
img = cv.imread('photos/s.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
kernel = np.ones((5,5),np.uint8)
# erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel,iterations = 1)

cv.imshow('img', dilation)
cv.waitKey(0)