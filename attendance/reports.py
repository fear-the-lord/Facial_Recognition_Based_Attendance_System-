#import module from tkinter for UI
from tkinter import *

import os

#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("600x600")

def function1():
    
    os.system("synopsis.docx")
    
def function4():

    root.destroy()
    os.system("python page1.py")

def function3():
	os.system("start .\final_presentation.pptx")

def function2():
	root.destroy()

#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="Project Reports",font=("times new roman",40),fg="white",bg="maroon",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating a button
Button(root,text="Synopsis",font=("times new roman",30),bg="#3F51B5",fg='white',command=function1).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="Presentation",font=("times new roman",30),bg="#3F51B5",fg='white',command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating second button
Button(root,text="Back",font=("times new roman",30),bg="#3F51B5",fg='white',command=function4).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=("times new roman",30),bg="maroon",fg='white',command=function2).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
