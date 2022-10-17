#Help https://youtu.be/H37f_x4wAC0
from datetime import datetime
start_time = datetime.now()

def octant_longest_subsequence_count_with_range():
###Code

 from openpyxl import load_workbook
 import os
 import numpy as np
 os.system('cls')

 time = [] #  new list for time
 v = []    #  new list for v
 u = []    #  new list for u
 w = []    #  new list for w
 vd = []    # list for difference of Vavg-v
 ud = []    # list for difference of Uavg-u
 wd = []    # list for difference of Wavg-w
 oct = []   # list for storing octant

 lwb=load_workbook("input_octant_longest_subsequence_with_range.xlsx")
 sheet=lwb["Sheet1"] 
 n=sheet.max_row
 for r in range(2,n+1):
  time.append(sheet.cell(row=r,column=1).value)
  u.append(sheet.cell(row=r,column=2).value)
  v.append(sheet.cell(row=r,column=3).value)
  w.append(sheet.cell(row=r,column=4).value)

 v_avg=np.mean(v, dtype=np.float64) # calculate  average of u
 u_avg=np.mean(u, dtype=np.float64) # calculate average of v
 w_avg=np.mean(w, dtype=np.float64) # calculate  average of w
 
 for r in range(2,n+1):
  ud.append(float(sheet.cell(row=r,column=2).value)-u_avg) # pushing  row[1]-Uavg in ud list
  vd.append(float(sheet.cell(row=r,column=3).value)-v_avg) # pushing row[2]-Vavg in vd list
  wd.append(float(sheet.cell(row=r,column=4).value)-w_avg)	# pushing  row[3]-Wavg in wd list 

 for i in range(0,n-1):# find octants
  if ((ud[i]>=0) and (vd[i]>=0) and (wd[i]>=0 )):
   oct.append(1)   # adding the octant in the oct list after checking the condition of octant 1 to calculate overall octant 1 value     
  elif((ud[i]>=0) and (vd[i]>=0) and (wd[i]<0 )):
   oct.append(-1)   # adding the octant in the oct list after checking the condition of octant -1 to calculate overall octant -1 value
  elif((ud[i]<0) and (vd[i]>=0) and (wd[i]>=0 )):
   oct.append(2)   # adding the octant in the oct list after checking the condition of octant 2 to calculate overall octant 2 value
  elif((ud[i]<0) and (vd[i]>=0) and (wd[i]<0 )):
   oct.append(-2)   # adding the octant in the oct list after checking the condition of octant -2 to calculate overall octant -2 value
  elif((ud[i]>=0) and (vd[i]<0) and (wd[i]>=0 )):
   oct.append(4)   # adding the octant in the oct list after checking the condition of octant 4 to calculate overall octant 4 value
  elif((ud[i]>=0) and (vd[i]<0) and (wd[i]<0 )):
   oct.append(-4)    # adding the octant in the oct list after checking the condition of octant -4 to calculate overall octant -4 value   
  elif((ud[i]<0) and (vd[i]<0) and (wd[i]>=0 )):
   oct.append(3)   # adding the octant in the oct list after checking the condition of octant 3 to calculate overall octant 3 value
  else:
   oct.append(-3)   # adding the octant in the oct list after checking the condition of octant -3 to calculate overall octant -3 value
 