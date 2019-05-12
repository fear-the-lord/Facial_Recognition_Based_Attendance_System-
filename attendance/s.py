from tkinter import *
from tkinter import ttk
import os
import tkinter
from tkinter import messagebox


window = Tk()
window.title("STUDENT SECTION")
window.resizable(0, 0) 
            
def function1():
    text = entry_id.get()  # get the text from entry
            # format the text on the invisible label you created above
    if text == '1' or text == '2' or text == '3' or text == '4':
            window.destroy()
            os.system('python student.py')
    else:
           root = tkinter.Tk()
           root.withdraw()
           messagebox.showinfo("Student Section", "Your ID is not correct ")
              
                                     # prohibit resizing the window

text = ttk.Label(window, text='Enter your Id:')
text.grid(row=0, column=0, sticky=W)
            #label_result = ttk.Label(window, text='Result:')
           # label_result.grid(row=1, column=0, sticky=W)
            # create an id for the invisible label where will be displayed the text in the box
label = StringVar()
            # create the invisible label
invisible_label = ttk.Label(window, text='', textvariable=label)
invisible_label.grid(row=1, column=1, sticky=E)

            # create an id for your entry, this helps getting the text
entry_id = StringVar()
entry = ttk.Entry(
window, textvariable=entry_id, justify=RIGHT)
entry.grid(row=0, column=1, sticky=E)

button = ttk.Button(window, text='Enter', command=function1)
button.grid(row=2, column=1, sticky=E)
          
window.mainloop()

        

