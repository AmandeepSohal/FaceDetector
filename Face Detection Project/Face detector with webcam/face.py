import cv2
from random import randrange

#use pre trained xml files 
faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#use webcam
webcam = cv2.VideoCapture(0)

#make this read the FRAME in the webcam until program is terminated
while True:

    #read FRAME
    successful_frame_read, frame = webcam.read()

    #turn gray scale for computer to use in the current FRAME
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #find the coords for any face which varries in size
    face_coordinates = faces.detectMultiScale(grayscale) 

    #create a constant rectangle around the face in the current FRAME
    #random rgb for rectangle, and size 10 border
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 10)

    #show the FRAME of the webcam 
    cv2.imshow("face", frame)

    #this makes the computer read the webcam every FRAME and displays the webcam
    key = cv2.waitKey(1)

    #to stop force quitting, user must hit ESC key to break the loop
    #ESC key was found with ASCII table (27 = ESC)
    if key == 27: 
        break

webcam.release()