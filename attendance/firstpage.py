#import module from tkinter for UI

from tkinter import *
from playsound import playsound
import os
import subprocess,sys
from datetime import datetime;
#from PIL import ImageTk, Image
#creating instance of TK
root=Tk()
photo = PhotoImage('imagexav.png')
l = Label(image = photo)
#l.pack()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    playsound('TextTo.mp3')
    os.system("python dataset_capture.py")
    playsound('S.mp3')
    
def function2():
    
    os.system("python training_dataSet.py")
    playsound('train.mp3')

def function3():

    os.system("python recognizer.py")
    playsound('sound.mp3')
   
def function6():

    root.destroy()
    os.system('python loginfaculty.py')

def attend():
    
    os.system('python m.py')

def function5():
	root.destroy()
	os.system('python reports.py')

def function():
    root.destroy()

#setting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
#Button(root,text="Create Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
#Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Send Attendance Sheet through Mail",font=('times new roman',20),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#Button(root,text="Project Reports",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Log Out",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=10,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function).grid(row=12,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
