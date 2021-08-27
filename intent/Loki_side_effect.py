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
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "dose": ["第一劑", "第二劑", "第三劑"], "Taiwan": ["台灣", "臺灣", "本島", "本國", "全台", "全台灣", "全臺灣", "全島", "全臺", "全臺各地", "全國"], "Medigen": ["高端", "medigen", "Medigen"], "Moderna": ["Moderna", "莫德納"], "leftover": ["剩餘", "剩餘量", "剩餘數", "剩量", "剩餘資料", "剩餘數字", "剩餘分佈", "剩餘分布","剩餘狀況","剩餘情形"], "syn_verb": ["出現", "有"], "side_effect": ["side_effect", "severe_side_effect"], "vaccine_verb": ["打完", "打過", "接種", "注射"], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "上海復興", "上海復興BNT", "輝瑞"]}
vaccineDICT = userDefinedDICT["AZ"] + userDefinedDICT["Moderna"] + userDefinedDICT["Pfizer-BioNTech"] + userDefinedDICT["Medigen"]

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_side_effect:
        print("[side_effect] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["vaccine_shot"] = []
    resultDICT["side_effect"] = []
    resultDICT["severe_side_effect"] = []
    if utterance == "[az][vaccine_shot]side_effect為何":
        if args[0] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[az]side_effect":
        if args[0] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[az]vaccine_shot[會][有]哪些side_effect":
        if args[0] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[打完][莫德納][後]，[出現]哪些severe_side_effect需要送醫":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["severe_side_effect"].append(hospitaldict[k])

    if utterance == "[打完][莫德納]vaccine_shot[後]，[出現]哪些severe_side_effect需要送醫":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["severe_side_effect"].append(hospitaldict[k])

    if utterance == "[第一劑][az][會][有]哪些side_effect":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])


    if utterance == "[第一劑][az]side_effect":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[第一劑][az]vaccine_shot[會][有]哪些side_effect":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[第一劑][az]vaccine_shotside_effect":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "請問[az]vaccine_shotside_effect為何":
        if args[0] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    return resultDICT