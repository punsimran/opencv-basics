import cv2 as cv 
import numpy as np

img = cv.imread('photos/image.png')
# blankimg
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 90, img.shape[0]//2 ) , 150,255 , -1)
# cv.imshow('mask', mask)

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)

comb = cv.bitwise_and(circle, rectangle)


masked = cv.bitwise_and(img, img, mask=comb)
cv.imshow('masked', masked)


# masked_not = cv.bitwise_not(img, img, mask=mask)
# cv.imshow('masked not', masked_not)


# masked_or = cv.bitwise_or(img, img, mask=mask)
# cv.imshow('masked or', masked_or)


# masked_xor = cv.bitwise_xor(img, img, mask=mask)
# cv.imshow('masked xor', masked_xor)
# cv.imshow("dog",img)
cv.waitKey(0)