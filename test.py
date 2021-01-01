<<<<<<< HEAD
import cv2 as cv 

# Showing Nolan Image
#img = cv.imread('photos/nolan.png')
#cv.imshow('Nolan', img)

# Reading Videos
capture = cv.VideoCapture(0)


cv.waitKey(0) 
=======
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
toufic = []

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

   
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


>>>>>>> d8af2c9e04fa868dd8dcd035700a49d3eeb62d90
