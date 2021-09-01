#!/usr/bin/env python
# -*- coding:utf-8 -*-

import covid_info_bot
import requests
import json
import pandas as pd
from pprint import pprint
import datetime as dt

vaccine_stock_url = 'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=2001'
'''
{"id":"ID",
"a01":"日期",
"a02":"縣市別",
"a03":"總人口數",
"a04":"新增接種人次",
"a05":"累計接種人次",
"a06":"疫苗覆蓋率 (%)",
"a07":"累計配送量 (劑)",
"a08":"剩餘量 (劑)",
"a09":"剩餘量 (%)",
"a10":"AZ新增接種人次",
"a11":"AZ累計接種人次",
"a12":"AZ疫苗覆蓋率 (%)",
"a13":"AZ累計配送量 (劑)",
"a14":"AZ剩餘量 (劑)",
"a15":"AZ剩餘量 (%)",
"a16":"Moderna新增接種人次",
"a17":"Moderna累計接種人次",
"a18":"Moderna疫苗覆蓋率 (%)",
"a19":"Moderna累計配送量 (劑)"
"a20":"Moderna剩餘量 (劑)",
"a21":"Moderna剩餘量 (%)"}
'''

vaccine_stock = requests.get(url = vaccine_stock_url, verify=True)
vaccine_stock_rawDF = pd.DataFrame(vaccine_stock.json())
vaccine_stockDF = vaccine_stock_rawDF[['a01','a02','a08','a14','a20']]
vaccine_stockDF = vaccine_stockDF.loc[vaccine_stockDF.a01==vaccine_stockDF.a01[0]]
print(vaccine_stockDF)
vaccine_stockDF = vaccine_stockDF
#vaccine_stockDICT = json.loads()


def parse_response(inputSTR):
    vaccine_stock_template ={
        'vaccine_shot',
        'location'
    }
    response = covid_info_bot.runLoki([inputSTR])
    if 'vaccine_shot' in response.keys():
        vaccine_stock_template["vaccine_shot"]=response["vaccine_shot"]
    if 'location' in response.keys():
        vaccine_stock_template["location"]=response["location"]
    if vaccine_stock_template["vaccine_shot"] == 'AZ':
        
    
    return response

if __name__ == "__main__":
    print(vaccine_stockDF)
    response = parse_response("台中剩下多少劑AZ疫苗")
    print(response)