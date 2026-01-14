# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
 
# BLUE = [255,0,0]
 
# img1 = cv.imread('photos/logo.png')
# assert img1 is not None, "file could not be read, check with os.path.exists()"
 
# replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
# reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
# reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
# wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
# constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
 
# plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
 
# plt.show()

import cv2 as cv
import os
import time

# Path to image folder
folder = "photos"

# Read image filenames
image_files = sorted(os.listdir(folder))

# Load first image to get size
img_prev = cv.imread(os.path.join(folder, image_files[0]))
h, w = img_prev.shape[:2]

cv.namedWindow("Slideshow", cv.WINDOW_NORMAL)

# Loop through images
for i in range(1, len(image_files)):
    img_next = cv.imread(os.path.join(folder, image_files[i]))

    # Resize to same size (important)
    img_next = cv.resize(img_next, (w, h))

    # Smooth transition
    for alpha in range(0, 101, 2):
        a = alpha / 100.0
        blended = cv.addWeighted(img_prev, 1 - a, img_next, a, 0)

        cv.imshow("Slideshow", blended)

        if cv.waitKey(30) & 0xFF == 27:
            cv.destroyAllWindows()
            exit()

    # Hold image for a moment
    cv.imshow("Slideshow", img_next)
    cv.waitKey(800)

    img_prev = img_next

cv.destroyAllWindows()
