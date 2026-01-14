import cv2 as cv
import numpy as np

blank = np.zeros((500,500), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

# AND: intersection
bit_and = cv.bitwise_and(rectangle, circle )
# cv.imshow('BITWISE AND', bit_and)

# OR:- non intersecting and intersecting
bit_or = cv.bitwise_or(rectangle, circle )
# cv.imshow('BITWISE OR', bit_or)

# XOR:- non intersecting
bit_xor = cv.bitwise_xor(rectangle, circle )
# cv.imshow('BITWISE XOR', bit_xor)

# NOT :- 
bit_not = cv.bitwise_not(rectangle)
cv.imshow('BITWISE NOT', bit_not)

bit_not_c = cv.bitwise_not(circle)
cv.imshow('BITWISE NOT CIRCLE', bit_not_c)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)
cv.waitKey(0)