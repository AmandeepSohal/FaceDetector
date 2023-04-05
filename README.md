# FaceDetector
This is a basic AI that uses pre trained data provided. By using haarcases, we can display a box around the detected face.

Face detector with image will detect a face(s) facing forwards in the image, and create a rectangle around the face

Face detector with webcam will detect a face(s) facing forwards in the webcam in real time and crete a constantly updating rectangle around the face(s)

What I learned:
How to read a .xml file with cv2

How to read and show images 

How to get the webcam display 

How to turn webcam/images to grayscale using COLOR_BGR2GRAY (I could also use -1,0,or 1 to as well if I wanted to)

How to get face coordinates and use detectMultiScale to detect things that vary in size (i.e faces)

How to use an algoritm to draw a rectangle on a face by using the image or frame, and then taking the coordinates of (x,y), (x+w, y+h), rgb colors, width of rectangle border

How to break the loop using waitKey and assigning it to a key, where then you assign key to a value in the ascii table where if pressed, the loop breaks

How to make the webcam update every frame by using waitKey(1)
