import cv2 as cv
import numpy as np

img = cv.imread('photos/paris.png', cv.IMREAD_GRAYSCALE)
# cv.imshow('Original', img)

lap = cv.Laplacian(img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

# cv.imshow('Laplacian', lap)


# Sobeel 
sobelx = cv.Sobel(img, cv.CV_64F, 1,0)
sobely = cv.Sobel(img, cv.CV_64F, 0,1)
solbel_comb = cv.bitwise_or(sobelx, sobely)

# cv.imshow('Sobel X', sobelx)
# cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel Combined', solbel_comb)

cany = cv.Canny(img, 150, 175)
cv.imshow('Canny', cany)


cv.waitKey(0)