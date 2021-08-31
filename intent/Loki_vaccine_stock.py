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
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "dose": ["第一劑", "第三劑", "第二劑"], "doze": ["第一劑", "第二劑", "第三劑"], "Taiwan": ["全台", "全台灣", "全國", "全島", "全臺", "全臺各地", "全臺灣", "台灣", "本國", "本島", "臺灣"], "Medigen": ["Medigen", "medigen", "高端"], "Moderna": ["Moderna", "莫德納"], "leftover": ["剩量", "剩餘", "剩餘分佈", "剩餘分布", "剩餘數", "剩餘數字", "剩餘資料", "剩餘量"], "syn_verb": ["有", "出現"], "side_effect": ["副作用", "嚴重副作用"], "vaccine_verb": ["注射", "接種", "打完", "打過"], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "上海復興", "上海復興BNT", "輝瑞"]}
vaccineDICT = userDefinedDICT["AZ"] + userDefinedDICT["Moderna"] + userDefinedDICT["Pfizer-BioNTech"] + userDefinedDICT["Medigen"]

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_vaccine_stock:
        print("[vaccine_stock] {} ===> {}".format(inputSTR, utterance))

def formalize_name(val, userDefinedDICT, resultDICT, resultSTR):
    '''
    Formalizes the name of user defined words.
    val (str): value from agrs
    userDefinedDICT (dict): user defined dict
    resultDICT (dict): result dict
    resultSTR (str): key of result dict
    '''
    count = 0
    for k in userDefinedDICT.keys():
        if val in userDefinedDICT[k]:
            if count == 0: resultDICT[resultSTR].append(k); count+=1
            if count > 1: print(f"Name Error: Duplicate Names! ({val})")

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT['type'] = []
    resultDICT['location'] = []

    if utterance == "[可以]幫[我]查詢[AZ]在[台北]的[剩餘量]":
        if args[4] in userDefinedDICT['leftover']:
            if args[2] in vaccineDICT: formalize_name(args[2], userDefinedDICT, resultDICT, 'type')
            resultDICT['location'].append(args[3])

    if utterance == "[可以]幫[我]查詢[AZ]疫苗在[台北]的[剩餘量]":
        if args[4] in userDefinedDICT['leftover']:
            if args[2] in vaccineDICT: formalize_name(args[2], userDefinedDICT, resultDICT, "vaccine_shot")
            resultDICT['location'].append(args[3])

    if utterance == "[可以]跟[我]講[台北]疫苗剩下多少嗎？":
        resultDICT['type'].append('all')
        resultDICT['location'].append(args[2])

    if utterance == "[台中]剩下多少[AZ]疫苗":
        if args[1] in vaccineDICT: formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
        resultDICT['location'].append(args[0])


    if utterance == "[台中]剩下多少[劑][AZ]疫苗":
        if args[2] in vaccineDICT: formalize_name(args[2], userDefinedDICT, resultDICT, "vaccine_shot")
        resultDICT['location'].append(args[0])

    if utterance == "[台中]剩下多少[劑]疫苗":
        resultDICT['type'].append('all')
        resultDICT['location'].append(args[0])

    if utterance == "[台中]剩下多少疫苗":
        resultDICT['type'].append('all')
        resultDICT['location'].append(args[0])

    if utterance == "[台北]還有幾[劑][AZ]疫苗？":
        if args[2] in vaccineDICT: formalize_name(args[2], userDefinedDICT, resultDICT, "vaccine_shot")
        resultDICT['location'].append(args[0])

    if utterance == "[台北]還有幾[劑]疫苗？":
        resultDICT['type'].append('all')
        resultDICT['location'].append(args[0])

    if utterance == "[我]想查詢[台北]疫苗[剩餘量]":
        if args[2] in userDefinedDICT['leftover']:
            resultDICT['type'].append('all')
            resultDICT['location'].append(args[1])

    if utterance == "[我]想知道[AZ]在[台北]的[剩餘量]":
        if args[3] in userDefinedDICT['leftover']:
            if args[1] in vaccineDICT: formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
            resultDICT['location'].append(args[2])

    if utterance == "[我]想知道[AZ]疫苗在[台北]的[剩餘量]":
        if args[3] in userDefinedDICT['leftover']:
            if args[1] in vaccineDICT: formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
            resultDICT['location'].append(args[2])

    if utterance == "[我]想知道[全臺][高端]疫苗[剩餘分佈]":
        if args[3] in userDefinedDICT['leftover']:
            if args[2] in vaccineDICT: formalize_name(args[2], userDefinedDICT, resultDICT, "vaccine_shot")
            resultDICT['location'].append(args[1])

    if utterance == "[我]想知道[全臺]疫苗[剩餘分佈]":
        if args[2] in userDefinedDICT['leftover']:
            resultDICT['type'].append('all')
            resultDICT['location'].append(args[1])

    if utterance == "[我]想知道[台北]疫苗[剩餘量]":
        if args[2] in userDefinedDICT['leftover']:
            resultDICT['type'].append('all')
            resultDICT['location'].append(args[1])

    if utterance == "[我]要查詢[AZ]在[台北]的[剩餘量]":
        if args[3] in userDefinedDICT['leftover']:
            if args[1] in vaccineDICT: formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
            resultDICT['location'].append(args[2])

    if utterance == "[我]要查詢[台北]疫苗[剩餘量]":
        if args[2] in userDefinedDICT['leftover']:
            resultDICT['type'].append('all')
            resultDICT['location'].append(args[1])

    if utterance == "[我]要知道[台北]疫苗[剩餘量]":
        if args[2] in userDefinedDICT['leftover']:
            resultDICT['type'].append('all')
            resultDICT['location'].append(args[1])


    if utterance == "[能]給[我][全台][AZ]疫苗[剩餘數]":
        if args[4] in userDefinedDICT['leftover']:
            if args[3] in vaccineDICT: formalize_name(args[3], userDefinedDICT, resultDICT, "vaccine_shot")
            resultDICT['location'].append(args[2])


    if utterance == "[能]給[我][全台]疫苗[剩餘數]":
        if args[3] in userDefinedDICT['leftover']:
            resultDICT['type'].append('all')
            resultDICT['location'].append(args[2])

    if utterance == "幫[我]查詢[AZ]在[台北]的[剩餘量]":
        if args[3] in userDefinedDICT['leftover']:
            if args[1] in vaccineDICT: formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
            resultDICT['location'].append(args[2])

    if utterance == "幫[我]查詢[AZ]疫苗在[台北]的[剩餘量]":
        if args[3] in userDefinedDICT['leftover']:
            if args[1] in vaccineDICT: formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
            resultDICT['location'].append(args[2])

    if utterance == "給[我][全台][AZ]疫苗[剩餘數]":
        if args[3] in userDefinedDICT['leftover']:
            if args[2] in vaccineDICT: formalize_name(args[2], userDefinedDICT, resultDICT, "vaccine_shot")
            resultDICT['location'].append(args[1])

    if utterance == "給[我][全台]疫苗[剩餘數]":
        if args[2] in userDefinedDICT['leftover']:
            resultDICT['type'].append('all')
            resultDICT['location'].append(args[1])


    return resultDICT