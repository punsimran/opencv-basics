import cv2 as cv
import numpy as np

# img = cv.imread('photos/women.png', cv.IMREAD_GRAYSCALE)

img = cv.imread('photos/group.png', cv.IMREAD_GRAYSCALE)

haar_cascade = cv.CascadeClassifier('haar_front.xml')
face_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=7)
print(f'Number of faces found = {len(face_rect)}')

for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
cv.imshow('Detected Faces', img)


# cv.imshow('gray', img)
cv.waitKey(0)