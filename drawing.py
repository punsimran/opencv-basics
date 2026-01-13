import numpy as np
import cv2 as cv
 
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
 
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode, img , temp_img
 
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        temp_img = img.copy()
 
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            temp_img = img.copy()
            if mode == True:
                cv.rectangle(temp_img,(ix,iy),(x,y),(0,255,0),1)
            else:
                cv.circle(temp_img,(x,y),5,(0,0,255),11)
 
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),1)
            
img = np.zeros((512,512,3), np.uint8)
temp_img = img.copy()

cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
 
while(1):
    cv.imshow('image',temp_img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
 
cv.destroyAllWindows()