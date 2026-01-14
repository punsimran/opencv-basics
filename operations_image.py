import numpy as np
import cv2 as cv
 
# img = cv.imread('photos/image.png')

# accessing and modifying pixel values
# px = img[100,100]
# print(px)

# blue = img[100,100,0]
# print(blue)

# # modify the pixel values the same way
# img[100,100]=[255,255,255]
# print(img[100,100])

# # accesing image properties
# print(img.shape)

# print(img.dtype)

# ROI

# fur = img[420:480, 510:570]

# img[310:370, 400:460] = fur

# spliting and merging image channels
# b, g, r = cv.split(img)
# img= cv.merge((b,g,r))

# b = img[:,:,0]

# Making borders for images(padding)

# x = np.uint8([250])
# y = np.uint8([10])

# print(cv.add(x,y))  #output: 260

# print(x+y) #output: [4]

# cv.imshow("Result", img)

# cv.waitKey(0)
# cv.destroyAllWindows()


# Arthimetic Operations:

# image blending:

# img1 = cv.imread('photos/image.png')
# img2 = cv.imread('photos/logo.png')

# # I want to put logo on top-left corner, So I create a ROI
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols]
 
# # Now create a mask of logo and create its inverse mask also
# img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
# ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
# mask_inv = cv.bitwise_not(mask)
 
# # Now black-out the area of logo in ROI
# img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
 
# # Take only region of logo from logo image.
# img2_fg = cv.bitwise_and(img2,img2,mask = mask)
 
# # Put logo in ROI and modify the main image
# dst = cv.add(img1_bg,img2_fg)
# img1[0:rows, 0:cols ] = dst
 
# cv.imshow('res',img1)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Performance mesurement & improvement techniques
# cv.getTickCount() -> return the number of clock-cycle after a reference event (like machine was switched on) to the  moment this function is called.
# cv.getTickFrequency-> returns the frequency of clock-cycles, or the number of clock-cycle per second. so to find the time of execution in seconds

# measuring performance 
# img1 = cv.imread('photos/image.png')

# e1 = cv.getTickCount()
# for i in range(5,49,2):
#     img1 = cv.medianBlur(img1, i)
# e2 = cv.getTickCount()
# time = (e2 - e1)/cv.getTickFrequency()
# print(time)

# default optimaization
