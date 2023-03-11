#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 00:19:53 2023

@author: thomasrael
"""

import xlsxwriter
import requests
from datetime import datetime
from datetime import timedelta



print("––––––––––––––––––––––")

# url = list(urllib.request.urlopen("https://masslandlords.net/policy/eviction-data/filings-week-ending-" + date))
# print (url)

# for i in range(len(url)):
#     print (str(url[i]))

W  = []
E  = []
C  = []
SE = []
NE = []
MS = []


date = "2020-10-24" 

url = (requests.get("https://masslandlords.net/policy/eviction-data/filings-week-ending-" + date)).text
urllist = url.split()


DIC = {} ##key: date, value: evictions 
j = 0
while j < 130: ### until when??
    
    
    url = (requests.get("https://masslandlords.net/policy/eviction-data/filings-week-ending-" + date)).text
    urllist = url.split()
    L = [0,0,0,0,0,0] 
    for i in range(len(urllist)): 
        if urllist[i] == "metro_south":
            # print("Metro South:" + urllist[i+1]) 
            L[5] = urllist[i+1]
            MS.append(urllist[i+1])  
        if urllist[i] == "eastern" and urllist[i+1] != "hampshire":  
            # print("Eastern:" + urllist[i+1])
            L[4] = urllist[i+1] 
            E.append(urllist[i+1]) 
        if urllist[i] == "western":
            # print("Western:" + urllist[i+1])
            L[3] = urllist[i+1]
            W.append(urllist[i+1]) 
        if urllist[i] == "southeast":                  
            # print("Southeast:" + urllist[i+1])
            L[2] = urllist[i+1]
            SE.append(urllist[i+1]) 
        if urllist[i] == "northeast":
            # print("Northeast:" + urllist[i+1])
            L[1] = urllist[i+1]
            NE.append(urllist[i+1]) 
        if urllist[i] == "central" and urllist [i-1] != "bmc":  
            # print("Central:" + urllist[i+1])
            L[0] = urllist[i+1]
            C.append(urllist[i+1]) 
        
        DIC[date] = L
        
    date = datetime.strptime(date, "%Y-%m-%d")    
    date += timedelta(days=7) 
    date = datetime.strftime(date, "%Y-%m-%d")    
        
    j += 1
print (DIC)


"/Users/thomasrael/Desktop/piq/school/2022/UROP/"


workbook = xlsxwriter.Workbook("weekly-filings.xlsx")
worksheet = workbook.add_worksheet("FILINGS")

for i in range(len(DIC.keys())):
    worksheet.write(i+1,0,list(DIC.keys())[i])
    for j in range(6):
        worksheet.write(i+1,j+1,DIC[list(DIC.keys())[i]][j])

workbook.close()


