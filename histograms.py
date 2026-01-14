import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/sunflower.png')
# blank = np.zeros(img.shape[:2], dtype='uint8')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# circle = cv.circle(blank.copy(), (img.shape[1]//2 , img.shape[0]//2 ) , 150,255 , -1)


# mask = cv.bitwise_and(gray, gray , mask=circle)
# cv.imshow('mask', mask)

# # Grayscale histo
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color histogram
blank = np.zeros(img.shape[:2], dtype='uint8')



mask = cv.circle(blank.copy(), (img.shape[1]//2 , img.shape[0]//2 ) , 150,255 , -1)


masked = cv.bitwise_and(img, img , mask=mask)
cv.imshow('mask', masked)


plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

colors = ('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])   
    
plt.show()

cv.waitKey(0)