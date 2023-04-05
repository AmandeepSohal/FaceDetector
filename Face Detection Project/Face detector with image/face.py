import cv2
from random import randrange

#use pre trained xml files 
faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#test image
img = cv2.imread("face.jpg")

#turn image to grayscale for computer 
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = faces.detectMultiScale(grayscale)

#for loop to make a rectangle on each face in the image
#use a random for the rgb using randrange(256)
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256), 10))

#show the image with a rectangle around the faces
cv2.imshow("face", img)

cv2.waitKey()
