# import cv2 as cv

# image = cv.imread('photos/image.png')

# def rescaleFrame(frame, scale=0.75):
#     width = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)
#     dim = (width, height)

#     return cv.resize(frame,dim, interpolation= cv.INTER_AREA)
# # for live video
# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(4,height)


# resized_img = rescaleFrame(image)
# cv.imshow('img',resized_img)

# cv.waitKey(0)

# capture = cv.VideoCapture('videos/puppy.webm')

# while True:
#     isTrue, frame = capture.read() #frame by frame

#     frame_resized = rescaleFrame(frame)

#     cv.imshow('Video',frame) #display each frame of the video
#     cv.imshow('Resize', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'): #if we click the d then the loop gonna break
#         break

# capture.release()
# cv.destroyAllWindows()




