import cv2, numpy as np;
import xlwrite
import time
import sys
from playsound import playsound
import tkinter
from tkinter import messagebox

start=time.time()
period=30
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer.yml');
flag = 0;
id=0;
filename='filename';
dict = {
            'item1': 1
} 
#font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);
        id,conf=recognizer.predict(roi_gray)
        if(conf < 70):
         if(id==1):
            id='Souvik Ghosh'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',1,id,'yes');
                dict[str(id)]=str(id);
            
                
         elif(id==2):
            id = 'Indranil Das'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 2, id, 'yes');
                dict[str(id)] = str(id);

         elif(id==3):
            id = 'Kingshuk Mukherjee'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 3, id, 'yes');
                dict[str(id)] = str(id);

         elif(id==4):
            id = 'Ki'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 4, id, 'yes');
                dict[str(id)] = str(id);

        else:
             id = 'Unknown, can not recognize'
             flag=flag+1
             cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2);
             cv2.putText(img,"Spoof Detected",(x,y-10),font,0.55,(120,255,120),1)
             break
        
        cv2.putText(img,str(id),(x,y-10),font,0.55,(120,255,120),1)
        #cv2.putText(img,"Your attendance has been accepted",(x,w),font,0.55,(120,255,120),1)
    image = cv2.resize(img,(1500,768))
    cv2.imshow('frame',image);
    #cv2.imshow('gray',gray);
    #if flag == 10:
       # playsound('transactionSound.mp3')
       # playsound('Spoof.mp3')
    if time.time()>start+period:
        playsound('sound.mp3')
        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();
