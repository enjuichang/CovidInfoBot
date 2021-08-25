#!/usr/bin/env python
# -*- coding:utf-8 -*-

import covid_info_bot
import requests

vaccine_stock_url = 'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=2001'

vaccine_stock = requests.get(url = vaccine_stock_url, verify=False)

print(vaccine_stock.content)

def parse_response(inputSTR):
    response = covid_info_bot.runLoki(inputSTR)
    return response