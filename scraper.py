#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from bs4 import BeautifulSoup
import requests
import datetime


START_DATE = "2020-10-24" 
page_content = requests.get("https://masslandlords.net/policy/eviction-data/filings-week-ending-" + START_DATE).text.split()

RESULTS_DICT = {}

L = {
    "W": 0,
    "E": 0,
    "C": 0,
    "SE": 0,
    "NE": 0,
    "MS": 0
}

for i in range(len(page_content)): 
    if page_content[i] == "metro_south":
        L["MS"] = page_content[i+1] 
    if page_content[i] == "eastern" and page_content[i+1] != "hampshire":
        L["E"] = page_content[i+1] 
    if page_content[i] == "western":
        L["W"] = page_content[i+1]
    if page_content[i] == "southeast":
        L["SE"] = page_content[i+1]
    if page_content[i] == "northeast":
        L["NE"] = page_content[i+1]
    if page_content[i] == "central" and page_content [i-1] != "bmc":
        L["MS"] = page_content[i+1]
    
    RESULTS_DICT[START_DATE] = L

print (RESULTS_DICT)