import numpy as np
import cv2


#this is the cascade we just made. Call what you want
closed_cascade = cv2.CascadeClassifier('cascade.xml')

#this is the cascade I downloded for stop signs
stop_cascade = cv2.CascadeClassifier('stopsign_classifier.xml')


# detecting from camera, so for Demo use a mobile showing the demo
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    closed_signs = closed_cascade.detectMultiScale(gray)
    stop_signs = stop_cascade.detectMultiScale(gray)
    
    # add this for all cascades
    for (x,y,w,h) in closed_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Road Closed',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    
    for (x,y,w,h) in stop_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Stop Sign',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
