#Python program to build security camera

#Import libraries
import cv2 as cv
import winsound
cam=cv.VideoCapture(0)   #Use current camera
while cam.isOpened():
    ret, frame1=cam.read()  #read frame first time
    ret, frame2=cam.read()  #read frame second time
    diff=cv.absdiff(frame1, frame2) #time difference between two frames
    gray=cv.cvtColor(diff, cv.COLOR_BGR2GRAY) #Gray form of image
    blur=cv.GaussianBlur(gray, (5, 5), 0)  #Blurs the image
    _, thresh=cv.threshold(blur, 20, 255, cv.THRESH_BINARY) #Remove noises and make edges sharp
    dilate=cv.dilate(thresh, None, iterations=3)  #Make things a bit bigger
    contours, _=cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) #Detect moving objects
    #cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)  #Draw shapes for moving objects on figure1
    for c in contours:
        if cv.contourArea(c)<5000:  #Detect area only above 5000
            continue
        x, y, w, h=cv.boundingRect(c)  #Detect corners of the rectangle
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2) #Draw rectangle around moving object
        winsound.Beep(500, 200)  #Beep if motion detected
    if cv.waitKey(10)==ord('q'):
        break
    cv.imshow('Vinayak Camera', frame1)