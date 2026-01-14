import cv2 as cv 
import numpy as np

img = cv.imread('photos/sunflower.png')
# kernels: no of rows & cols

# Averaging:- compute the middle of pixel and average of surrounding of pixrls
average_blur = cv.blur(img, (5,5)) ##kernel size- 3,3
# cv.imshow("avg blur", average_blur)

# Gaussian Blur: each surrounding pixel have each weight but its natural
gaussian_blur = cv.GaussianBlur(img, (5,5), 0)
# cv.imshow('Gaussian Blur', gaussian_blur)

# Median Blur:- it finds the median of surronding pixels and also remove the noises
median_blur = cv.medianBlur(img, 5 ) #ksize : int
# cv.imshow('median blur', median_blur)

# Bilateral Blur:- retains the edges
bilateral_blur  = cv.bilateralFilter(img, 5, 45, 55)
cv.imshow('Bilateral blur', bilateral_blur)
cv.imshow('orginal', img)

cv.waitKey(0)