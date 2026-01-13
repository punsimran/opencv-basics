import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("photos/nature.png")

# plt.imshow(img)
# plt.show

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grayscale', gray)


# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

# BGR to LAB

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb',rgb)

# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('hsvtobgr', hsv_bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('labtobgr', lab_bgr)

cv.waitKey(0)
