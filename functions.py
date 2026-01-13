import cv2 as cv

img = cv.imread("photos/image.png")
 
# convert into grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('grayscale', gray)

# blur
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

#edge cascade
# canny = cv.Canny(img,125,175) # instead of img - blur to hide edges
# cv.imshow('Canny',canny)

# # Dilating the img 
# dilated= cv.dilate(canny, (3,3), iterations=1)  #iteration - thicker and (3,3)- more detailed and enhanced edges
# cv.imshow('dilated', dilated)

# # enroding
# eroded = cv.erode(dilated,(3,3),iterations=1)
# cv.imshow('erode', eroded)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('reshape', resized)

# crop
crop= img[50:250, 300:500]
cv.imshow('cropped', crop)

# cv.imshow('Dog', img)
cv.waitKey(0)