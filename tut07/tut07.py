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

        ######### Count of octants
        c1 = 0 
        c2 = 0  
        c3 = 0 
        c4 = 0  
        c5 = 0 
        c6 = 0  
        c7 = 0 
        c8 = 0  # It will give the count for octant -4

        # This list will store the starting time for longest subsequence length for octants
 

        for r in range(0, n-1):
            if oct[r] == 1:
                lon_s1 = lon_s1+1
                if r == n-2:
                    if lon_s1 > a:
                        a = lon_s1
                        lon_s1 = 0
                        c1 = 1
                    elif a > lon_s1:
                        lon_s1 = 0
                    else:
                        lon_s1 = 0
                        c1 = c1+1
            else:
                if lon_s1 > a:
                    a = lon_s1
                    lon_s1 = 0
                    c1 = 1
                elif a > lon_s1:
                    lon_s1 = 0
                else:
                    lon_s1 = 0
                    c1 = c1+1
        cn = 0 
		t1 = [] 
        for r in range(0, n-1):
            if oct[r] == 1:
                if cn == 0:
                    ti1 = time[r]
                cn = cn+1
            else:
                cn = 0
            if cn == a:  
                t1.append(ti1)
                cn = 0

                
        for r in range(0, n-1):
            if oct[r] == -1:
                lon_s2 = lon_s2+1
                if r == n-2:
                    if lon_s2 > b:
                        b = lon_s2
                        lon_s2 = 0
                        c2 = 1
                    elif b > lon_s2:
                        lon_s2 = 0
                    else:
                        lon_s2 = 0
                        c2 = c2+1
            else:
                if lon_s2 > b:
                    b = lon_s2
                    lon_s2 = 0
                    c2 = 1
                elif b > lon_s2:
                    lon_s2 = 0
                else:
                    lon_s2 = 0
                    c2 = c2+1

        cn = 0 
		t2 =[] 
        for r in range(0, n-1):
            if oct[r] == -1:
                if cn == 0:
                    ti2 = time[r]
                cn = cn+1
            else:
                cn = 0
            if cn == b:  
                t2.append(ti2)
                cn = 0

        for r in range(0, n-1):
            if oct[r] == 2:
                lon_s3 = lon_s3+1
                if r == n-2:
                    if lon_s3 > c:
                        c = lon_s3
                        lon_s3 = 0
                        c3 = 1
                    elif c > lon_s3:
                        lon_s3 = 0
                    else:
                        lon_s3 = 0
                        c3 = c3+1
            else:
                if lon_s3 > c:
                    c = lon_s3
                    lon_s3 = 0
                    c3 = 1
                elif c > lon_s3:
                    lon_s3 = 0
                else:
                    lon_s3 = 0
                    c3 = c3+1
        cn = 0  
		t3 = []
        for r in range(0, n-1):
            if oct[r] == 2:
                if cn == 0:
                    ti3 = time[r]
                cn = cn+1
            else:
                cn = 0
            if cn == c:  
                t3.append(ti3)
                cn = 0

        for r in range(0, n-1):
            if oct[r] == -2:
                lon_s4 = lon_s4+1
                if r == n-2:
                    if lon_s4 > d:
                        d = lon_s4
                        lon_s4 = 0
                        c4 = 1
                    elif d > lon_s4:
                        lon_s4 = 0
                    else:
                        lon_s4 = 0
                        c4 = c4+1
            else:
                if lon_s4 > d:
                    d = lon_s4
                    lon_s4 = 0
                    c4 = 1
                elif d > lon_s4:
                    lon_s4 = 0
                else:
                    lon_s4 = 0
                    c4 = c4+1
            
        cn = 0 
		t4 = [] 
        for r in range(0, n-1):
            if oct[r] == -2:
                if cn == 0:
                    ti4 = time[r]
                cn = cn+1
            else:
                cn = 0
            if cn == d:  
                t4.append(ti4)
                cn = 0

        for r in range(0, n-1):
            if oct[r] == 3:
                lon_s5 = lon_s5+1
                if r == n-2:
                    if lon_s5 > e:
                        e = lon_s5
                        lon_s5 = 0
                        c5 = 1
                    elif e > lon_s5:
                        lon_s5 = 0
                    else:
                        lon_s5 = 0
                        c5 = c5+1
            else:
                if lon_s5 > e:
                    e = lon_s5
                    lon_s5 = 0
                    c5 = 1
                elif e > lon_s5:
                    lon_s5 = 0
                else:
                    lon_s5 = 0
                    c5 = c5+1
            
        cn = 0  
		t5 = []
        for r in range(0, n-1):
            if oct[r] == 3:
                if cn == 0:
                    ti5 = time[r]
                cn = cn+1
            else:
                cn = 0
            if cn == e:  
                t5.append(ti5)
                cn = 0

        for r in range(0, n-1):
            if oct[r] == -3:
                lon_s6 = lon_s6+1
                if r == n-2:
                    if lon_s6 > a:
                        f = lon_s6
                        lon_s6 = 0
                        c6 = 1
                    elif f > lon_s6:
                        lon_s6 = 0
                    else:
                        lon_s6 = 0
                        c6 = c6+1
            else:
                if lon_s6 > f:
                    f = lon_s6
                    lon_s6 = 0
                    c6 = 1
                elif f > lon_s6:
                    lon_s6 = 0
                else:
                    lon_s6 = 0
                    c6 = c6+1
            
        cn = 0  
		t6 = []
        for r in range(0, n-1):
            if oct[r] == -3:
                if cn == 0:
                    ti6 = time[r]
                cn = cn+1
            else:
                cn = 0
            if cn == f:  
                t6.append(ti6)
                cn = 0

        for r in range(0, n-1):
            if oct[r] == 4:
                lon_s7 = lon_s7+1
                if r == n-2:
                    if lon_s7 > g:
                        g = lon_s7
                        lon_s7 = 0
                        c7 = 1
                    elif g > lon_s7:
                        lon_s7 = 0
                    else:
                        lon_s7 = 0
                        c7 = c7+1
            else:
                if lon_s7 > g:
                    g = lon_s7
                    lon_s7 = 0
                    c7 = 1
                elif g > lon_s7:
                    lon_s7 = 0
                else:
                    lon_s7 = 0
                    c7 = c7+1
        cn = 0  
		t7 = []
        for r in range(0, n-1):
            if oct[r] == 4:
                if cn == 0:
                    ti7 = time[r]
                cn = cn+1
            else:
                cn = 0
            if cn == g:  
                t7.append(ti7)
                cn = 0

        for r in range(0, n-1):
            if oct[r] == -4:
                lon_s8 = lon_s8+1
                if r == n-2:
                    if lon_s8 > a:
                        h = lon_s8
                        lon_s8 = 0
                        c8 = 1
                    elif h > lon_s8:
                        lon_s8 = 0
                    else:
                        lon_s8 = 0
                        c8 = c8+1
            else:
                if lon_s8 > h:
                    h = lon_s8
                    lon_s8 = 0
                    c8 = 1
                elif h > lon_s8:
                    lon_s8 = 0
                else:
                    lon_s8 = 0
                    c8 = c8+1
        cn = 0 
		t8 = [] 
        for r in range(0, n-1):
            if oct[r] == -4:
                if cn == 0:
                    ti8 = time[r]
                cn = cn+1
            else:
                cn = 0
            if cn == h:  
                t8.append(ti8)
                cn = 0

        tu3.append(["Octant##", "Longest Subsequence length", "Count"])
        tu3.append(["1", a, c1])
        tu3.append(["-1", b, c2])
        tu3.append(["2", c, c3])
        tu3.append(["-2", d, c4])
        tu3.append(["3", e, c5])
        tu3.append(["-3", f, c6])
        tu3.append(["4", g, c7])
        tu3.append(["-4", h, c8])
        for i in range(0, 1000):
            tu3.append(["", "", ""])
        
        ########  printing the first column the new requireduired table
        col_1 = []  
        col_1.append("Octant###")
        col_1.append("1")
        col_1.append("Time")
        for i in range(0, c1):  
            col_1.append("")
        col_1.append("-1")
        col_1.append("Time")
        for i in range(0, c2):  
            col_1.append("")
        col_1.append("2")
        col_1.append("Time")
        for i in range(0, c3):  
            col_1.append("")
        col_1.append("-2")
        col_1.append("Time")
        for i in range(0, c4):  
            col_1.append("")
        col_1.append("3")
        col_1.append("Time")
        for i in range(0, c5):  
            col_1.append("")
        col_1.append("-3")
        col_1.append("Time")
        for i in range(0, c6):  
            col_1.append("")
        col_1.append("4")
        col_1.append("Time")
        for i in range(0, c7):  
            col_1.append("")
        col_1.append("-4")
        col_1.append("Time")
        for i in range(0, c8):  
            col_1.append("")
        v = len(col_1)

        ########printing the second coloumn new requireduired table
        col_2 = []  
        col_2.append("Longest Subsequence Length")
        col_2.append(a)
        col_2.append("From")
        
        for i in range(0, c1):
            col_2.append(t1[i])
        col_2.append(b)
        col_2.append("From")
        
        for i in range(0, c2):
            col_2.append(t2[i])
        col_2.append(c)
        col_2.append("From")
        
        for i in range(0, c3):
            col_2.append(t3[i])
        col_2.append(d)
        col_2.append("From")
        
        for i in range(0, c4):
            col_2.append(t4[i])
        col_2.append(e)
        col_2.append("From")
        
        for i in range(0, c5):
            col_2.append(t5[i])
        col_2.append(f)
        col_2.append("From")
        
        for i in range(0, c6):
            col_2.append(t6[i])
        col_2.append(g)
        col_2.append("From")

        for i in range(0, c7):
            col_2.append(t7[i])
        col_2.append(h)
        col_2.append("From")

        for i in range(0, c8):
            col_2.append(t8[i])

        ########  printing third coloumn the new requireduired table
        col_3 = []  
        col_3.append("Count")
        col_3.append(c1)
        col_3.append("To")
        
        for i in range(0, c1):
            col_3.append(t1[i] + 0.01*(a-1))
        col_3.append(c2)
        col_3.append("To")
        
        for i in range(0, c2):
            col_3.append(t2[i] + 0.01*(b-1))
        col_3.append(c3)
        col_3.append("To")
        
        for i in range(0, c3):
            col_3.append(t3[i] + 0.01*(c-1))
        col_3.append(c4)
        col_3.append("To")
        
        for i in range(0, c4):
            col_3.append(t4[i] + 0.01*(d-1))
        col_3.append(c5)
        col_3.append("To")
        
        for i in range(0, c5):
            col_3.append(t5[i] + 0.01*(e-1))
        col_3.append(c6)
        col_3.append("To")
        
        for i in range(0, c6):
            col_3.append(t6[i] + 0.01*(f-1))
        col_3.append(c7)
        col_3.append("To")
        
        for i in range(0, c7):
            col_3.append(t7[i] + 0.01*(g-1))
        col_3.append(c8)
        col_3.append("To")
        
        for i in range(0, c8):
            col_3.append(t8[i] + 0.01*(h-1))

        for i in range(0, 1000):
            col_1.append("")
            col_2.append("")
            col_3.append("")
