import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_front.xml')
fav = ['taylor', 'selena','daniel', 'frank']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')


img = cv.imread('model/frank/1.jpeg', cv.IMREAD_GRAYSCALE)
cv.imshow('org', img)

face_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

for (x,y,w,h) in face_rect:
    face_roi = img[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(face_roi)   
    print(f'Label: {fav[label]}, Confidence: {confidence}')
    cv.putText(img, str(fav[label]), (x,y-10), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)
