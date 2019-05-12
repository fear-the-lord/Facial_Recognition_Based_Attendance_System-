#import module from tkinter for UI
from tkinter import *
from playsound import playsound
import os
from datetime import datetime;
import subprocess,sys
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.startfile(os.getcwd()+"\\attendance"+str(datetime.now().date())+'.xls')

def function2():
    
    root.destroy()
    os.system("python page1.py")

#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="View Attendance",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="Back",font=('times new roman',20),bg="maroon",fg="white",command=function2).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
