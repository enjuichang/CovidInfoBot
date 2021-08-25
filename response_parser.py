#!/usr/bin/env python
# -*- coding:utf-8 -*-

import covid_info_bot
import requests
import json

vaccine_stock_url = 'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=2001'

vaccine_stock = requests.get(url = vaccine_stock_url, verify=False)

#vaccine_stockDICT = json.loads(vaccine_stock.json())


def parse_response(inputSTR):
    response = covid_info_bot.runLoki([inputSTR])
    return response

if __name__ == "__main__":
    response = parse_response("打完az疫苗後，出現哪些嚴重副作用需要送醫")
    print(response)