from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import os
# make database and users (if not exists already) table at programme start up
with sqlite3.connect('databasefaculty.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

# root = tk.Tk ()
# root.configure(background="white") 

# title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#main Class
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('databasefaculty.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            #self.logf.pack_forget()
            #self.head['text'] = self.username.get() + '\n Loged In'
            #self.head['pady'] = 150
            root.destroy()
            os.system('python firstpage.py')
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('databasefaculty.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'FACULTY SIGNUP PAGE'
        self.crf.pack()

    def function1(self):
        root.destroy()
        os.system("python page1.py")
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'FACULTY LOGIN PAGE',font = ('times new roman',35),padx=5,pady = 10,bg="maroon",fg="white")
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'USERNAME: ',font = ('times new roman',20),bg="maroon",fg="white").grid(row=1,sticky = N+E+W+S,padx=5,pady=5)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('times new roman',15),bg="black",fg="white").grid(row=1,rowspan=2,columnspan=2,column=2,padx=5,pady=5)
        Label(self.logf,text = 'PASSWORD: ',font = ('times new roman',20),bg="maroon",fg="white").grid(row=3,sticky = N+E+W+S,padx=5,pady=5)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*',bg="black",fg="white").grid(row=3,rowspan=2,columnspan=1,column=2,padx=5,pady=5)
        Button(self.logf,text = 'Login ',bd = 3 ,font = ('times new roman',20),padx=5,pady=5,command=self.login,bg="#0D47A1",fg="white").grid(row=7,columnspan=5,sticky=N+E+W+S,padx=5,pady=5)
        Button(self.logf,text = ' Back ',bd = 3 ,font = ('times new roman',20),padx=5,pady=5,bg="maroon",fg="white",command=self.function1).grid(row=11,columnspan=5,sticky=N+E+W+S,padx=5,pady=5)

        self.logf.pack()
        
        self.crf = Label(self.master,text='FACULTY SIGNUP PAGE',font=('times new roman',35),padx =5,pady = 10,bg='white',fg='white')
        Label(self.crf,text = 'Username: ',font = ('times new roman',20),bg='maroon',fg='white').grid(row=1,sticky = N+E+W+S,padx=5,pady=5)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('times new roman',15),bg='black',fg='white').grid(row=1,rowspan=2,columnspan=2,column=2,padx=5,pady=5)
        Label(self.crf,text = 'Password: ',font = ('times new roman',20),pady=5,padx=5,bg='maroon',fg='white').grid(row=3,sticky = N+E+W+S,padx=5,pady=5)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*',bg='black',fg='white').grid(row=3,column=2,rowspan=2,columnspan=1,padx=5,pady=5)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('times new roman',20),padx=5,pady=5,command=self.new_user,bg="#0D47A1",fg="white").grid(row=9,columnspan=5,sticky=N+E+W+S,padx=5,pady=5)
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('times new roman',20),padx=5,pady=5,command=self.log,bg="#0D47A1",fg="white").grid(row=11,columnspan=5,sticky=N+E+W+S,padx=5,pady=5)
        Button(self.crf,text = ' Back ',bd = 3 ,font = ('times new roman',20),padx=5,pady=5,bg="maroon",fg="white",command=self.function1).grid(row=13,columnspan=5,sticky=N+E+W+S,padx=5,pady=5)

    

#create window and application object
root = Tk()
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
root.configure(background="white") 
main(root)
root.mainloop()
