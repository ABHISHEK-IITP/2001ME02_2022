def octact_identification(mod=5000):
 import csv
 import os
 import numpy as np
 os.system('cls')
 time = []  # new list for time
 v = []     # new list for V
 u = []     # new list for U
 w = []     # new list for W
 vd = []    # list for difference of Vavg - V
 ud = []    # list for difference of Uavg -U
 wd = []    # list for difference of Wavg - W
 oct = []   # list for storing octant

 with open('octant_input.csv', 'r') as file:
  reader = csv.reader(file)
  r = 0
  for row in reader:
   if (r == 0):
    r = r+1 #continue only for r==0
   else:
    time.append(row[0]) # push row[0] in time
    u.append(row[1])    # push row[1] in u    
    v.append(row[2])    # push row[2] in v
    w.append(row[3])    # push row[3] in w
  v_avg=np.mean(v, dtype=np.float64) #  calculate average of v
  u_avg=np.mean(u, dtype=np.float64) #  calculate average of u
  w_avg=np.mean(w, dtype=np.float64) #  calculate average of w

 with open('octant_input.csv', 'r') as file: # opening input file
  reader = csv.reader(file)
  m=0
  for row in reader:
   if (m==0):
    m=m+1
   else:
    ud.append(float(row[1])-u_avg)     # push row[1] - U_avg in ud list
    vd.append(float(row[2])-v_avg)     # push row[2] - V_avg in vd list
    wd.append(float(row[3])-w_avg)     # push row[3] - W_avg	in wd list

 with open('octant_input.csv', 'r') as file: # opening input file for counting rows 
  reader = csv.reader(file)
  i=0
  for row in reader:
   i=i+1
  n=i # n is number of rows
  n=n-1
  print(n) # print value of number of rows
 with open('octant_input.csv', 'r') as file: # again opening the input file for octant 
  reader = csv.reader(file)  
 	
  for i in range(n):# using this for loop we will get octant
   if (i<n-1):
    if ((ud[i]>=0) and (vd[i]>=0) and (wd[i]>=0 )):
     oct.append(1)         # adding the octant in oct list after checking the condition of octant 1 to calculate overall octant 1 value
    elif((ud[i]>=0) and (vd[i]>=0) and (wd[i]<0 )):
     oct.append(-1)         # adding the octant in oct list after checking the condition of octant -1 to calculate overall octant -1 value
    elif((ud[i]<0) and (vd[i]>=0) and (wd[i]>=0 )):
     oct.append(2)         # adding the octant in oct list after checking the condition of octant 2 to calculate overall octant 2 value
    elif((ud[i]<0) and (vd[i]>=0) and (wd[i]<0 )):
     oct.append(-2)         # adding the octant in oct list after checking the condition of octant -2 to calculate overall octant -2 value
    elif((ud[i]>=0) and (vd[i]<0) and (wd[i]>=0 )):
     oct.append(4)         # adding the octant in oct list after checking the condition of octant to 4 calculate overall octant 4 value
    elif((ud[i]>=0) and (vd[i]<0) and (wd[i]<0 )):
     oct.append(-4)         # adding the octant in oct list after checking the condition of octant to -4 calculate overall octant -4 value    
    elif((ud[i]<0) and (vd[i]<0) and (wd[i]>=0 )):
     oct.append(3)         # adding the octant in oct list after checking the condition of octant 3 to calculate overall octant 3 value
    else:
     oct.append(-3)          # adding the octant in oct list after checking the condition of octant -3 to calculate overall octant -3 value

 with open('octant_input.csv', 'r') as file: # again opening the input file for overall count of octant 
  reader = csv.reader(file)  
  i=0
  count1=0         # calculating total count of octant 1
  count3=0         # calculating total count of octant 2
  count2=0         # calculating total count of octant -1
  count4=0         # calculating total count of octant -2
  count5=0         # calculating total count of octant 3
  count6=0         # calculating total count of octant -3
  count7=0         # calculating total count of octant 4
  count8=0         # calculating total count of octant -4	 
  for i in range(n):       # for loop to calculate count of octants
   if (i<n-1):
    if (oct[i]==1):
     count1=count1+1
    elif(oct[i]==-1):
     count2=count2+1
    elif(oct[i]==2):
     count3=count3+1
    elif(oct[i]==-2):
     count4=count4+1
    elif(oct[i]==3):
     count5=count5+1
    elif(oct[i]==-3):
     count6=count6+1    
    elif(oct[i]==4):
     count7=count7+1
    else:
     count8=count8+1
    i=i+1  
 count1_mod=[]                   ## calculating total count of octant in mod range 1 
 count2_mod=[]                   ## calculating total count of octant in mod range 2
 count3_mod=[]                   ## calculating total count of octant in mod range -1
 count4_mod=[]                   ## calculating total count of octant in mod range -2
 count5_mod=[]                   ## calculating total count of octant in mod range 3
 count6_mod=[]                   ## calculating total count of octant in mod range -3
 count7_mod=[]                   ## calculating total count of octant in mod range 4
 count8_mod=[]                   ## calculating total count of octant in mod range -4
 with open('octant_input.csv', 'r') as file: # opening the file to calculate total count of octant in mod range
  reader = csv.reader(file)
  i=0
  r=0
  octant1=0
  octant2=0
  octant3=0
  octant4=0
  octant5=0
  octant6=0
  octant7=0
  octant8=0
  m= int((n-1)/mod) +1
  for i in range(m):
   s=mod*i
   for r in range(mod):	 # for loop to calculate individual count of octants in range of mod
    if(r+s<n-1):	                                    
     if (oct[r+s]==1):
      octant1=octant1+1    #calculate count of octant 1 in range of particular mod
     elif(oct[r+s]==-1):
      octant2=octant2+1    #calculate count of octant -1 in range of particular mod
     elif(oct[r+s]==2):
      octant3=octant3+1    #calculate count of octant 2 in range of particular mod
     elif(oct[r+s]==-2):
      octant4=octant4+1    #calculate count of octant -2 in range of particular mod
     elif(oct[r+s]==3):
      octant5=octant5+1    #calculate count of octant 3 in range of particular mod
     elif(oct[r+s]==-3):
      octant6=octant6+1     #calculate count of octant -3 in range of particular mod   
     elif(oct[r+s]==4):
      octant7=octant7+1    #calculate count of octant 4 in range of particular mod
     elif(oct[r+s]==-4):
      octant8=octant8+1    #calculate count of octant -4 in range of particular mod 
   count1_mod.append(octant1) # push values of count of octant 1 in particular raneg of mod
   count2_mod.append(octant2) # push values of count of octant -1 in particular raneg of mod
   count3_mod.append(octant3) # push values of count of octant 2 in particular raneg of mod
   count4_mod.append(octant4) # push values of count of octant -2 in particular raneg of mod
   count5_mod.append(octant5) # push values of count of octant 3 in particular raneg of mod
   count6_mod.append(octant6) # push values of count of octant -3 in particular raneg of mod
   count7_mod.append(octant7) # push values of count of octant 4 in particular raneg of mod
   count8_mod.append(octant8) # push values of count of octant -4 in particular raneg of mod
   octant1=0
   octant2=0
   octant3=0
   octant4=0
   octant5=0
   octant6=0
   octant7=0
   octant8=0
 print(count1_mod)
 with open('octant_output.csv','w',newline="") as file:
  writer=csv.writer(file)
  writer.writerow(["Time",'U','V','W','Uavg','Vavg','Wavg',"U'=U-Uavg","V'=V-Vavg","W'=W-Wavg","Octant","","OctantID","+1","-1","+2","-2","+3","-3","+4","-4"])
  r=0
  for x in range(n-1):
   if(x==0):
    writer.writerow([time[x],u[x],v[x],w[x],u_avg,v_avg,w_avg,ud[x],vd[x],wd[x],oct[x],"","Overall count",count1,count2,count3,count4,count5,count6,count7,count8])
   elif(x==1):
    s="mod "+str(mod)		
    writer.writerow([time[x],u[x],v[x],w[x],"","","",ud[x],vd[x],wd[x],oct[x],"User input",s,"","","","","","","",""])
   elif(x>=2 and x<2+m):
    if(x==1+m):
     z=r*mod 	
     y=(r+1)*mod
     s=str(z)+"-"+str(n)		 
     writer.writerow([time[x],u[x],v[x],w[x],"","","",ud[x],vd[x],wd[x],oct[x],"",s,count1_mod[x-2],count2_mod[x-2],count3_mod[x-2],count4_mod[x-2],count5_mod[x-2],count6_mod[x-2],count7_mod[x-2],count8_mod[x-2]])	 
     r=r+1
    else:
     z=r*mod	
     y=(r+1)*mod-1
     s=str(z)+"-"+str(y)		 
     writer.writerow([time[x],u[x],v[x],w[x],"","","",ud[x],vd[x],wd[x],oct[x],"",s,count1_mod[x-2],count2_mod[x-2],count3_mod[x-2],count4_mod[x-2],count5_mod[x-2],count6_mod[x-2],count7_mod[x-2],count8_mod[x-2]])	 
     r=r+1
   else:
    writer.writerow([time[x],u[x],v[x],w[x],"","","",ud[x],vd[x],wd[x],oct[x],"","","","","","","","","",""])			 
mod = 5000
octact_identification(mod)