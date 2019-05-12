import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import tkinter
from tkinter import messagebox
import sqlite3
from datetime import datetime;

final =""
conn=sqlite3.connect('databaseadmin.db')
c = conn.cursor()

r = ('SELECT COUNT(username) FROM user')

c.execute(r)
f = c.fetchone()
for s in f:
   for i in range(1,s+1):
       usern = ('SELECT username FROM user where rowid='+str(i))
       c.execute(usern)
       result = c.fetchone()
       for row in result:
           final = final + row+ " " 
           
 
conn.close()
   
fromaddr = "souvikghosh199831@gmail.com"
li = list(final.split(" "))
toaddr = li
 
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = ','.join(toaddr)
  
# storing the subject  
msg['Subject'] = "Attendance Sheet"
  
# string to store the body of the mail 
body = "Highly Confidential"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "attendance"+str(datetime.now().date())+'.xls'
attachment = open("attendance"+str(datetime.now().date())+'.xls', "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "souvik31") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 

root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("Msg Sent", "Your mail has been sent successfully")
