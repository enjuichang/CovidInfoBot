#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for vaccine_stock

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_vaccine_stock = True
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "dose": ["第一劑", "第二劑", "第三劑"], "Taiwan": ["台灣", "臺灣", "本島", "本國", "全台", "全台灣", "全臺灣", "全島", "全臺", "全臺各地", "全國"], "Medigen": ["高端", "medigen", "Medigen"], "Moderna": ["Moderna", "莫德納"], "leftover": ["剩餘", "剩餘量", "剩餘數", "剩量", "剩餘資料", "剩餘數字", "剩餘分佈", "剩餘分布"], "syn_verb": ["出現", "有"], "side_effect": ["副作用", "嚴重副作用"], "vaccine_verb": ["打完", "打過", "接種", "注射"], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "上海復興", "上海復興BNT", "輝瑞"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_vaccine_stock:
        print("[vaccine_stock] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[可以]幫[我]查詢[AZ]在[台北]的[剩餘量]":
        # write your code here
        pass

    if utterance == "[可以]幫[我]查詢[AZ]疫苗在[台北]的[剩餘量]":
        # write your code here
        pass

    if utterance == "[可以]跟[我]講[台北]疫苗剩下多少嗎？":
        # write your code here
        pass

    if utterance == "[台中]剩下多少[AZ]疫苗":
        # write your code here
        pass

    if utterance == "[台中]剩下多少[劑][AZ]疫苗":
        # write your code here
        pass

    if utterance == "[台中]剩下多少[劑]疫苗":
        # write your code here
        pass

    if utterance == "[台中]剩下多少疫苗":
        # write your code here
        pass

    if utterance == "[台北]還有幾[劑][AZ]疫苗？":
        # write your code here
        pass

    if utterance == "[台北]還有幾[劑]疫苗？":
        # write your code here
        pass

    if utterance == "[我]想查詢[台北]疫苗[剩餘量]":
        # write your code here
        pass

    if utterance == "[我]想知道[AZ]在[台北]的[剩餘量]":
        # write your code here
        pass

    if utterance == "[我]想知道[AZ]疫苗在[台北]的[剩餘量]":
        # write your code here
        pass

    if utterance == "[我]想知道[全臺][高端]疫苗[剩餘分佈]":
        # write your code here
        pass

    if utterance == "[我]想知道[全臺]疫苗[剩餘分佈]":
        # write your code here
        pass

    if utterance == "[我]想知道[台北]疫苗[剩餘量]":
        # write your code here
        pass

    if utterance == "[我]要查詢[AZ]在[台北]的[剩餘量]":
        # write your code here
        pass

    if utterance == "[我]要查詢[台北]疫苗[剩餘量]":
        # write your code here
        pass

    if utterance == "[我]要知道[台北]疫苗[剩餘量]":
        # write your code here
        pass

    if utterance == "[能]給[我][全台][AZ]疫苗[剩餘數]":
        # write your code here
        pass

    if utterance == "[能]給[我][全台]疫苗[剩餘數]":
        # write your code here
        pass

    if utterance == "幫[我]查詢[AZ]在[台北]的[剩餘量]":
        # write your code here
        pass

    if utterance == "幫[我]查詢[AZ]疫苗在[台北]的[剩餘量]":
        # write your code here
        pass

    if utterance == "給[我][全台][AZ]疫苗[剩餘數]":
        # write your code here
        pass

    if utterance == "給[我][全台]疫苗[剩餘數]":
        # write your code here
        pass

    return resultDICT