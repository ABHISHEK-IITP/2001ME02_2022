

from datetime import datetime
from unicodedata import name
start_time = datetime.now()

def attendance_report():
###Code
#importing required libraries
 import csv 
 import os  
 import numpy as np 
 os.system('cls')
 roll_number=[] #list of students' roll number
 stud_name=[] #list of students' name

 with open('input_registered_students.csv', 'r') as file: #opening file of registered students
  reader = csv.reader(file)
  n=0
  for row in reader:
   if n!=0:
    roll_number.append(row[0])  # list of registered students' roll NO.
    stud_name.append(row[1])   # list of registered Students' Name
   n=n+1 
  n=n-1
 dat =["28-07","01-08","04-08","08-08","11-08","15-08","18-08","22-08","25-08","29-08","01-09","05-09","08-09","12-09","15-09","26-09","29-09"]
 # date on which class was conducted
 s=len(dat) # total dates


 with open('input_attendance.csv', 'r') as file: #opening attendance file
  reader = csv.reader(file) 
  
  tot_dat=[] # List of full data of students
  Stud_data=[] # List of full data of Particular student
  st=[] # List of full data of  a particular Student on a particular date 
  for x in roll_number:
   Stud_data=[] # Initializing Stud data
   for j in dat:
    st=[] # Initializing st(total attendance)
    Real_Att=0 #initialising Real attandence of student
    Dup_Att=0  #initialising Duplicate attendance of student
    Fake_Att=0  #initailising Fake attendance of student
    with open('input_attendance.csv', 'r') as file: #opening attendance file again
     reader = csv.reader(file)
     for row in reader:
      if j==row[0][0:5] and row[1][0:8]==x and (row[0][11:13]=="14" or row[0][11:16]=="15:00" ) and Real_Att==0 : 
       Real_Att=Real_Att+1 # Updating real attendance of student
      elif j==row[0][0:5] and row[1][0:8]==x and (row[0][11:13]=="14" or row[0][11:16]=="15:00") and Real_Att>0 : 
       Dup_Att=Dup_Att+1 # Updating Duplicate attendance of student 
      elif j==row[0][0:5] and row[1][0:8]==x :
       Fake_Att=Fake_Att+1 # Updating Fake attendance of student
     st.append(Real_Att+Dup_Att+Fake_Att)   #appending total attendance
     st.append(Real_Att)  # appending real attendance
     st.append(Dup_Att)   # appending Duplicate attendance
     st.append(Fake_Att)  # appending Fake attendance
     if Real_Att==0:
      st.append(1)
     else:
      st.append(0) 
    Stud_data.append(st)
   tot_dat.append(Stud_data)
 
 if os.path.exists("output"):
  for f in os.listdir("output"):
    os.remove(os.path.join("output",f)) # removing all the prebuild files in output folder

 os.chdir("output")
 from openpyxl import Workbook
 for i in range(0,n): 
  book=Workbook()
  sheet= book.active    
  rows=[] # Making of list of rows of a particular student of all dates
  rows.append(["Date","Roll No.","Name","Total attendance count","Real","Duplicate","Invalid","absent"])
  rows.append(["",roll_number[i],stud_name[i],"","","","",""])
  for q in range(0,s):
   rows.append([dat[q],"","",tot_dat[i][q][0],tot_dat[i][q][1],tot_dat[i][q][2],tot_dat[i][q][3],tot_dat[i][q][4]]) # Appending all types of Attendance in row
  for w in rows:
   sheet.append(w)
  book.save( roll_number[i] + ".xlsx") # Saving attendance of a particular student
   
  dic={0:"A",1:"P"} # Dictionary for present and absent
  book=Workbook()
  sheet= book.active    
  rows=[]
  z=["Roll No.","Name"] # Initializing 1st row
  for i in dat: # Initializing 1st row
   z.append(i)
  z.append("Total Lecture taken") 
  z.append("Total Real")
  z.append("% Attendance")
  rows.append(z) 

  z=["(Sorted by roll no.)","","Atleast one real P"] # Initializing 2nd row
  for i in range(0,s-1): # using this loop we are making 2nd row
   z.append("")
  z.append("(=Total Mon+Thur dynamic count")
  z.append("")
  z.append("Real/Actual Lecture taken")
  rows.append(z) 

  for i in range(0,n):  # using this loop i am making full data of all the students
   z=[roll_number[i],stud_name[i]]
   Stud_data=0
   for q in range(0,s):
    z.append(dic[tot_dat[i][q][1]]) #total lecture taken
    if dic[tot_dat[i][q][1]]=="P":
     Stud_data=Stud_data+1
   z.append(s)
   z.append(Stud_data) 
   l=(Stud_data/s)*100
   z.append("{:.2f}".format(l))
   rows.append(z)

  for w in rows:
   sheet.append(w)
  try:
   book.save( "Attendance_report_consolidated" + ".xlsx")  # Saving full attendance report
  except:
    print("Error")


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()
# importing required libraries for sending mail
import smtplib
import email.encoders
import base64

from email.encoders import encode_base64
from getpass import getpass
from smtplib import SMTP
    
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mimetypes import guess_type
    


            
def send_mail(): #defining function to send mail
    fromaddr = input("Enter Mail Id: ") #taking mail id from mail is to be sent
    toaddr = "cs3842022@gmail.com"  #reciever's mail id
    Password_ = input("Enter Password: ")  #generated password of sender's mail id 

   
    msg = MIMEMultipart()    #  MIMEMultipart
    msg['From'] = fromaddr    # sender's mail id
    msg['To'] = toaddr    # receiver's email address
    msg['Subject'] = "Tut06 attendance report"   # Subject of mail
    body = "Dear Sir,\n\nPlease find attachment.\n\nThanks and Regards\nAbhishek\n2001ME02" #message of mail
    msg.attach(MIMEText(body, 'plain')) #attachment 

    filename = 'attendance_report_consolidated.xlsx'  #attachment
    attachment = open("attendance_report_consolidated.xlsx", "rb") #opening attachment

    p = MIMEBase('application', 'octet-stream')   # instance of MIMEBase and named as p

    p.set_payload((attachment).read())    # To change the payload into encoded form

    encoders.encode_base64(p)             # encode into base64

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)    # attach the file with message

    s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session

    s.starttls()     

    s.login(fromaddr, Password_)    # login sender

    text = msg.as_string()      # Converts the Multipart msg into a string

    s.sendmail(fromaddr, toaddr, text)  # sending the mail
    s.quit()



send_mail()   #Running function to send mail
print("*****************************************************     run successfully     ******************************************************")



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
