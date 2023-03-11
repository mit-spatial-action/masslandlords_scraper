#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 00:19:53 2023

@author: thomasrael
"""

import requests
from datetime import datetime
from datetime import timedelta
import csv


print("––––––––––––––––––––––")

# W  = []
# E  = []
# C  = []
# SE = []
# NE = []
# MS = []


date = "2020-10-24" 

url = (requests.get("https://masslandlords.net/policy/eviction-data/filings-week-ending-" + date)).text
urllist = url.split()


DIC = {} ##key: date, value: [date, central, noreast,soueast,western,eastern,msouth]
j = 0
while j < 130: ### until when??
    
    
    url = (requests.get("https://masslandlords.net/policy/eviction-data/filings-week-ending-" + date)).text
    urllist = url.split()
    L = [date,0,0,0,0,0,0] 
    for i in range(len(urllist)): 
        if urllist[i] == "metro_south":
            # print("Metro South:" + urllist[i+1]) 
            L[6] = urllist[i+1]
            # MS.append(urllist[i+1])  
        if urllist[i] == "eastern" and urllist[i+1] != "hampshire":  
            # print("Eastern:" + urllist[i+1])
            L[5] = urllist[i+1] 
            # E.append(urllist[i+1]) 
        if urllist[i] == "western":
            # print("Western:" + urllist[i+1])
            L[4] = urllist[i+1]
            # W.append(urllist[i+1]) 
        if urllist[i] == "southeast":                  
            # print("Southeast:" + urllist[i+1])
            L[3] = urllist[i+1]
            # SE.append(urllist[i+1]) 
        if urllist[i] == "northeast":
            # print("Northeast:" + urllist[i+1])
            L[2] = urllist[i+1]
            # NE.append(urllist[i+1]) 
        if urllist[i] == "central" and urllist [i-1] != "bmc":  
            # print("Central:" + urllist[i+1])
            L[1] = urllist[i+1]
            # C.append(urllist[i+1]) 
        
        DIC[date] = L
        
    date = datetime.strptime(date, "%Y-%m-%d")  #turn date string into date format  
    date += timedelta(days=7) # forward 1 week (next wecord)
    date = datetime.strftime(date, "%Y-%m-%d")  #turn date format back into date string to affix to URL
        
    j += 1 #counter
# print (DIC)

fields = ["DATE", "Central", "Northeast", "Southeast", "Western", "Eastern", "Metro-South"] 
    
# data rows of csv file 
rows = list(DIC.values())
    
# name of csv file 
filename = "weekly-filings-cambridge.csv"
    
# writing to csv file 
with open(filename, "w") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)




