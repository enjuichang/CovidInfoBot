#!/usr/bin/env python
# -*- coding:utf-8 -*-

import covid_info_bot
import requests

import certifi
# import urllib3

# http = urllib3.PoolManager(
#     cert_reqs="CERT_REQUIRED",
#     ca_certs=certifi.where()
# )

# vaccine_stock_url = 'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=2001'
test_url = "https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=5001&limited=全部縣市"

vaccine_stock_url = "https://covid-19.nchc.org.tw/api/covid19"
#vaccine_stock_api = requests.get(url = vaccine_stock_url, verify=certifi.where())
vaccine_stock_api = requests.post(url=vaccine_stock_url, data = {"CK":"covid-19@nchc.org.tw", "querydata":"5001", "limited":"全部縣市"})

print(vaccine_stock_api)

def parse_response(inputSTR):
    response = covid_info_bot.runLoki(inputSTR)
    return response