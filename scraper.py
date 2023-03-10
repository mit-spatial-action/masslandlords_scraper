#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 00:19:53 2023

@author: thomasrael
"""

from bs4 import BeautifulSoup
import xlsxwriter



print("––––––––––––––––––––––")



W = []
E = []
C = []
SE = []
NE = []
MS = []
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
years = ["2020","2021","2022","2023"]

DIC = {}

for y in years:
    for m in months:
        for d1 in range(4):
            for d10 in range(10):
                date = str(y + "-" + m + "-" + str(d1) + str(d10))
                L = [0,0,0,0,0,0]
                try: ## change directory access manually V  change yearly input manually V
                    with open("/Users/thomasrael/Desktop/piq/school/2022/UROP/filings/weekly/filings-week-ending-" + date + ".html") as fp:
                        soup = BeautifulSoup(fp)
                        souplist = str(soup).split()
                    
                        for i in range(len(souplist)):
                            try: 
                                if souplist[i] == "eastern" and souplist[i+1] != "hampshire":  
                                    # print("Eastern:" + souplist[i+1])
                                    L[4] = souplist[i+1] 
                                    E.append(souplist[i+1]) 
                                if souplist[i] == "northeast":
                                    # print("Northeast:" + souplist[i+1])
                                    L[1] = souplist[i+1]
                                    NE.append(souplist[i+1]) 
                                if souplist[i] == "western":
                                    # print("Western:" + souplist[i+1])
                                    L[3] = souplist[i+1]
                                    W.append(souplist[i+1]) 
                                if souplist[i] == "central" and souplist [i-1] != "bmc":  
                                    # print("Central:" + souplist[i+1])
                                    L[0] = souplist[i+1]
                                    C.append(souplist[i+1]) 
                                if souplist[i] == "southeast":                  
                                    # print("Southeast:" + souplist[i+1])
                                    L[2] = souplist[i+1]
                                    SE.append(souplist[i+1]) 
                                if souplist[i] == "metro_south":
                                    # print("Metro South:" + souplist[i+1])
                                    L[5] = souplist[i+1]
                                    MS.append(souplist[i+1]) 
                            except:
                                continue
                        DIC[date] = L 
                except:
                    continue
            # print (date)
# print ("C:" + str(C))
# print("––––––––––––––––––––––")
# print ("NE:" + str(NE))
# print("––––––––––––––––––––––")
# print ("SE:" + str(SE))
# print("––––––––––––––––––––––")
# print ("W:" + str(W))
# print("––––––––––––––––––––––")
# print ("E:" + str(E))
# print("––––––––––––––––––––––")
# print ("MS:" +  str(MS))
# print("––––––––––––––––––––––")
print (DIC)
# print (len(DIC))

"/Users/thomasrael/Desktop/piq/school/2022/UROP/"


workbook = xlsxwriter.Workbook("weekly-filings.xlsx")
worksheet = workbook.add_worksheet("FILINGS")

for i in range(len(DIC.keys())):
    worksheet.write(i+1,0,list(DIC.keys())[i])
    for j in range(6):
        worksheet.write(i+1,j+1,DIC[list(DIC.keys())[i]][j])

workbook.close()


