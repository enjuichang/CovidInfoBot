#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for side_effect

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json

with open("json/side_effect.json", mode="r", encoding="utf-8") as file:
    sideeffectDict = json.loads(file.read())

with open("json/hospital_immediately.json", mode="r", encoding="utf-8") as f:
    hospitaldict = json.loads(f.read())

DEBUG_side_effect = True
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "dose": ["第一劑", "第三劑", "第二劑"], "doze": ["第一劑", "第二劑", "第三劑"], "Taiwan": ["全台", "全台灣", "全國", "全島", "全臺", "全臺各地", "全臺灣", "台灣", "本國", "本島", "臺灣"], "Medigen": ["Medigen", "medigen", "高端"], "Moderna": ["Moderna", "莫德納"], "leftover": ["剩量", "剩餘", "剩餘分佈", "剩餘分布", "剩餘數", "剩餘數字", "剩餘資料", "剩餘量"], "syn_verb": ["有", "出現"], "side_effect": ["副作用", "嚴重副作用"], "vaccine_verb": ["注射", "接種", "打完", "打過"], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "上海復興", "上海復興BNT", "輝瑞"]}
vaccineDICT = userDefinedDICT["AZ"] + userDefinedDICT["Moderna"] + userDefinedDICT["Pfizer-BioNTech"] + userDefinedDICT["Medigen"]

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_side_effect:
        print("[side_effect] {} ===> {}".format(inputSTR, utterance))

def formalize_name(val, userDefinedDICT, resultDICT, resultSTR):
    count = 0
    for k in userDefinedDICT.keys():
        if val in userDefinedDICT[k]:
            if count == 0: resultDICT[resultSTR].append(k); count+=1
            if count > 1: print(f"Name Error: Duplicate Names! ({val})")

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["vaccine_shot"] = []
    resultDICT["side_effect"] = []
    resultDICT["severe_side_effect"] = []

    if utterance == "[az]疫苗[副作用]為何":
        if args[0] in vaccineDICT:
            formalize_name(args[0], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[1] == "副作用":
            resultDICT["side_effect"].append(args[1])

    if utterance == "[az][副作用]":
        if args[0] in vaccineDICT:
            formalize_name(args[0], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[1] == "副作用":
            resultDICT["side_effect"].append(args[1])

    if utterance == "[az]疫苗[會]有哪些[副作用]":
        if args[0] in vaccineDICT:
            formalize_name(args[0], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[2] == "副作用":
            resultDICT["side_effect"].append(args[2])

    if utterance == "[打完][莫德納][後]，[出現]哪些[嚴重副作用]需要送醫":
        if args[1] in vaccineDICT:
            formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[4] == "嚴重副作用":
            resultDICT["severe_side_effect"].append(args[4])

    if utterance == "[打完][莫德納]疫苗[後]，[出現]哪些[嚴重副作用]需要送醫":
        if args[1] in vaccineDICT:
            formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[4] == "嚴重副作用":
            resultDICT["severe_side_effect"].append(args[4])

    if utterance == "[第一劑][az][會]有哪些[副作用]":
        if args[1] in vaccineDICT:
            formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[3] == "副作用":
            resultDICT["side_effect"].append(args[3])


    if utterance == "[第一劑][az][副作用]":
        if args[1] in vaccineDICT:
            formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[2] == "副作用":
            resultDICT["side_effect"].append(args[2])

    if utterance == "[第一劑][az]疫苗[會][有]哪些[副作用]":
        if args[1] in vaccineDICT:
            formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[4] == "副作用":
            resultDICT["side_effect"].append(args[4])

    if utterance == "[第一劑][az]疫苗[副作用]":
        if args[1] in vaccineDICT:
            formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[2] == "副作用":
            resultDICT["side_effect"].append(args[2])

    if utterance == "請問[az]疫苗[副作用]為何":
        if args[0] in vaccineDICT:
            formalize_name(args[0], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[1] == "副作用":
            resultDICT["side_effect"].append(args[1])

    if utterance == "[第一劑][az][會]有哪些[副作用]":
        if args[1] in vaccineDICT:
            formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[3] == "副作用":
            resultDICT["side_effect"].append(args[3])
            

    if utterance == "[第一劑][az]疫苗[會]有哪些[副作用]":
        if args[1] in vaccineDICT:
            formalize_name(args[1], userDefinedDICT, resultDICT, "vaccine_shot")
        if args[3] == "副作用":
            resultDICT["side_effect"].append(args[3])
    

    return resultDICT