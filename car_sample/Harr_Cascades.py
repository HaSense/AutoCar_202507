import cv2
from pop import Util

Util.enable_imshow()

haar_face= '/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_face)

cam = Util.gstrmer(width=640, height=480)
camera = cv2.VideoCapture(cam, cv2.CAP_GSTREAMER)
if not camera.isOpened():
    print("Not found camera")

for _ in range(300):
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray, scaleFactor=1.3 ,minNeighbors=1,minSize=(100,100))
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)

cam.release()
cv2.destroyAllWindows()
