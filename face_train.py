import os
import cv2 as cv
import numpy as np

fav = ['taylor', 'selena','daniel', 'frank']

DIR = r'/home/simranpun/opencv/model'

haar_cascade = cv.CascadeClassifier('haar_front.xml')


features = []
labels = []
def create_train():
    for  person in fav:
        path = os.path.join(DIR, person)
        label = fav.index(person)

        for imgname in os.listdir(path):
            img_path = os.path.join(path, imgname)
            img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

            face_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in face_rect:
                faces_roi = img[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
print('Training done ------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)


