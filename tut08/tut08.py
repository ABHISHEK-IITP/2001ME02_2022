
from datetime import datetime
start_time = datetime.now()

#Help
def scorecard():
	pass


###Code
####importing required libraries
import openpyxl
import pandas as pd
import os

#reading input files
india_inn = open("india_inns2.txt","r+") #india batting
pak_inn = open("pak_inns1.txt","r+") #pakistan batting
Playing_XI = open("teams.txt","r+")
input_team = Playing_XI.readlines()

pak_team = input_team[0]
pak_players = pak_team[23:-1:].split(",")

ind_team = input_team[2]
ind_players = ind_team[20:-1:].split(",")


lst_ind=india_inn.readlines() #124
for i in lst_ind:
    if i=='\n':
        lst_ind.remove(i)
      

lst_pak=pak_inn.readlines() #123
for i in lst_pak:
    if i=='\n':
        lst_pak.remove(i)

wb = openpyxl.Workbook()
sheet = wb.active

# batting [runs,ball,4s,6s,sr]
# bowling [over,medan,runs,Wickets, NB, WD, ECO]
#declaring required variables
FOW_ind=0
FOW_pak=0
Pak_out_count={}
ind_bowlers={}
ind_bats={}

pak_bats={}
pak_bowlers={}
pak_byes=0
Pak_bowlers_score=0
