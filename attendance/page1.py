#import tkinter as tk
from tkinter import *
import os
from datetime import datetime;

root = Tk ()
root.configure(background="white") 

def function6():

    root.destroy()

def function1():

   root.destroy()
   os.system("python page2.py")

def function2():

   root.destroy()
   os.system("python loginadmin.py")

def function5():
	root.destroy()
	os.system('python reports.py')

def function3():
	root.destroy()
	os.system('python s.py')

root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
Button(root,text="Faculty",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Admin",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Student",font=("times new roman",20),bg="#0D47A1",fg='white',command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Project Reports",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
