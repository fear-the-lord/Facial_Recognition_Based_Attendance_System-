from tkinter import *
import os
from datetime import datetime;

root = Tk ()
root.configure(background="white")

def function6():

    root.destroy()

def function1():
 
   root.destroy()
   os.system("python loginfaculty.py")

def function2():

	root.destroy()
	os.system("python page1.py")

root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
Button(root,text="Login",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Back",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root, text="FACULTY RESPONSE",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)

root.mainloop()
