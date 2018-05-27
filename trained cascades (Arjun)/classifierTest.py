import numpy as np
import cv2


#this is the cascade we just made. Call what you want
#closed_cascade = cv2.CascadeClassifier('cascade.xml')

#this is the cascade I downloded for stop signs 
#stop_cascade = cv2.CascadeClassifier('stopsign_classifier.xml')

#this is the cascade for stop signs (Arjun)
stop_cascade = cv2.CascadeClassifier('cascade_stop_stage13.xml')

#this is the cascade for noTurnText (Arjun)
noTurn_cascade = cv2.CascadeClassifier('cascade_noTurnText_stage9.xml')

#this is the cascade for oneWayLeft (Arjun)
oneWayLeft_cascade = cv2.CascadeClassifier('cascade_oneWayLeft_stage12.xml')

#this is the cascade for oneWayRight (Arjun)
oneWayRight_cascade = cv2.CascadeClassifier('cascade_oneWayRight_stage14.xml')

# detecting from camera, so for Demo use a mobile showing the demo
cap = cv2.VideoCapture(0)

#From a video
#cap = cv2.VideoCapture('20180517_183501.mp4')

while 1:
    ret, img = cap.read()
    
    #ROI = img[40:440, 0:640]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)

    #closed_signs = closed_cascade.detectMultiScale(gray)
    stop_signs = stop_cascade.detectMultiScale(gray)
    noTurn_signs = noTurn_cascade.detectMultiScale(gray)
    oneWayLeft_signs = oneWayLeft_cascade.detectMultiScale(gray)
    oneWayRight_signs = oneWayRight_cascade.detectMultiScale(gray)

    # add this for all cascades
      #for (x,y,w,h) in closed_signs:
       # cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img,'Road Closed',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    
    #for (x,y,w,h) in stop_signs:
     #   cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
      #  font = cv2.FONT_HERSHEY_SIMPLEX
       # cv2.putText(img,'Stop Sign',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)

    for (x,y,w,h) in stop_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Stop Sign',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    
    for (x,y,w,h) in noTurn_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'No Turn',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)

    for (x,y,w,h) in oneWayLeft_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'One-Way Left',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)

    for (x,y,w,h) in oneWayRight_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'One-Way Right',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)

    cv2.imshow('img',img)
    k = cv2.waitKey(25) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
