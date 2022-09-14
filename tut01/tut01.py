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