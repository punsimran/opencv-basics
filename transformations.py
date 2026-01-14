import cv2 as cv
import numpy as np

img = cv.imread('photos/image.png')
# cv.imshow('Dog', img)

# translations
# def translate(img, x, y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dim = (img.shape[1],img.shape[0])
#     return cv.warpAffine(img, transMat, dim)

# translated = translate(img, -100,-100)
# cv.imshow('translate', translated)

# # rotations
# def rotate(img,angle, rotPoint=None):
#     (height, width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint= (width//2, height//2)

#     rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)
#     dim = (width, height)

#     return cv.warpAffine(img, rotMat, dim)

# rotated = rotate(img, 65)
# cv.imshow("rotate", rotated)

# rotated_rotated = rotate(rotated, -45)
# cv.imshow('rotated', rotated_rotated)

# resizing
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

# # flipping
# flip = cv.flip(img, -1)
# cv.imshow('flipped', flip)

# # cropping
# cropped = img[200:400 , 300:400]
# cv.imshow('crop', cropped)

cv.waitKey(0)