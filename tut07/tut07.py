from datetime import datetime
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles.borders import Border, Side
start_time = datetime.now()

# Help


def octant_analysis(mod=5000):
    from openpyxl import load_workbook
    import os
    import numpy as np
    from operator import itemgetter

    os.system('cls')
    curr = os.getcwd()  
    if os.path.exists("output"):
        for f in os.listdir("output"):  
            os.remove(os.path.join("output", f))
        os.rmdir("output")  # delete output folder
    os.mkdir(curr.replace('\\', '/')+"/output/")  # make output folder
    os.chdir("input")
    fil = os. listdir()  # storing all file name of input folder in list
    os.chdir(curr)
    for list in fil:
        print(list)
        os.chdir("input")  # taking input
        wb = load_workbook(list)
        sheet = wb.active

        ######### making  new lists ##########
        time = []  
        v = []   
        u = []   
        w = []   

        # making  lists for difference
        vd = []    
        ud = []    
        wd = []    
        oct = []    # make a list for octant stori
        wb = load_workbook(list)

        sheet = wb.active
        n = sheet.max_row  
        for r in range(2, n+1):       
            time.append(sheet.cell(row=r, column=1).value)
            u.append(sheet.cell(row=r, column=2).value)
            # making of w list from given data
            v.append(sheet.cell(row=r, column=3).value)
            w.append(sheet.cell(row=r, column=4).value)
        
        ########### Calculating mean v,u,w
        v_mean = np.mean(v, dtype=np.float64)  
        u_mean = np.mean(u, dtype=np.float64) 
        w_mean = np.mean(w, dtype=np.float64) 

        for r in range(2, n+1):
            ud.append(float(sheet.cell(row=r, column=2).value) -
                      u_mean)  
            vd.append(float(sheet.cell(row=r, column=3).value) -
                      v_mean)  
            wd.append(float(sheet.cell(row=r, column=4).value) -
                      w_mean)  
        tu3 = []

        ######### Getting octant     
        for i in range(0, n-1):  
            if ((ud[i] >= 0) and (vd[i] >= 0) and (wd[i] >= 0)):
                oct.append(1)
            elif ((ud[i] >= 0) and (vd[i] >= 0) and (wd[i] < 0)):
                oct.append(-1)
            elif ((ud[i] < 0) and (vd[i] >= 0) and (wd[i] >= 0)):
                oct.append(2)
            elif ((ud[i] < 0) and (vd[i] >= 0) and (wd[i] < 0)):
                oct.append(-2)
            elif ((ud[i] >= 0) and (vd[i] < 0) and (wd[i] >= 0)):
                oct.append(4)
            elif ((ud[i] >= 0) and (vd[i] < 0) and (wd[i] < 0)):
                oct.append(-4)
            elif ((ud[i] < 0) and (vd[i] < 0) and (wd[i] >= 0)):
                oct.append(3)
            else:
                oct.append(-3)
        
        ######## Declaring variables for storing the longest subsequence value of octant -1
        lon_s1 = 0  
        lon_s2 = 0 
        lon_s3 = 0 
        lon_s4 = 0  
        lon_s5 = 0 
        lon_s6 = 0  
        lon_s7 = 0 
        lon_s8 = 0  

        ########### Declaring variables giving the longest subsequence length for octants
        a = 0  
        b = 0  
        c = 0 
        d = 0  
        e = 0 
        f = 0  
        g = 0 
        h = 0  
