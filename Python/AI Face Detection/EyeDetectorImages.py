import cv2
from random import randrange

trainedEyeData = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('EM.jpg')

grayScaledImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Allows colours to be represented in less bits also. Takes the image as an argument as well as the conversion type.

#Detect Eyes
eyesCoordinates = trainedEyeData.detectMultiScale(grayScaledImg)
print(eyesCoordinates) #Stored in a 2d list.

for (x,y,w,h) in eyesCoordinates: #Searches for faces.
    cv2.rectangle(img, (x,y),(x+w,y+h), (randrange(256),randrange(256),randrange(256)), 2) #Draws the rectangle for each face found. Uses random colours.

cv2.imshow('Eye Detector', img) #Shows the image for a split second, titles the window, staticImage is the image to be shown.
cv2.waitKey() #Stops the image from closing instantly. Pauses the execution of code. Closes onclick of a key.

print("Code completed") #Indicates that the code ran sucessfully.