import cv2 as cv

#For image
# image = cv.imread('photos/image.png')

# cv.imshow('Puppy',image) #display the img as a new window

# cv.waitKey(0) #inifinte amount of the time

#For video
capture = cv.VideoCapture('videos/puppy.webm')

while True:
    isTrue, frame = capture.read() #frame by frame
    cv.imshow('Video',frame) #display each frame of the video

    if cv.waitKey(20) & 0xFF==ord('d'): #if we click the d then the loop gonna break
        break

capture.release()
cv.destroyAllWindows()



