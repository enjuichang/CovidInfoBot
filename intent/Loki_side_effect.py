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

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["vaccine_shot"] = []
    resultDICT["side_effect"] = []
    resultDICT["severe_side_effect"] = []
    if utterance == "[az][疫苗]副作用為何":
        if args[0] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[az]副作用":
        if args[0] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[az]疫苗[會][有]哪些副作用":
        if args[0] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[打完][莫德納][後]，[出現]哪些嚴重副作用需要送醫":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["severe_side_effect"].append(hospitaldict[k])

    if utterance == "[打完][莫德納]疫苗[後]，[出現]哪些嚴重副作用需要送醫":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["severe_side_effect"].append(hospitaldict[k])

    if utterance == "[第一劑][az][會][有]哪些副作用":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])


    if utterance == "[第一劑][az]副作用":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[第一劑][az]疫苗[會][有]哪些副作用":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "[第一劑][az]疫苗副作用":
        if args[1] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])

    if utterance == "請問[az]疫苗副作用為何":
        if args[0] in vaccineDICT:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["vaccine_shot"].append(k)
                    resultDICT["side_effect"].append(sideeffectDict[k])
    if utterance == "[az]嚴重副作用":
        # write your code here
        pass

    if utterance == "az疫苗[會]有哪些副作用":
        # write your code here
        pass

    if utterance == "第一劑az[會]有哪些副作用":
        # write your code here
        pass

    if utterance == "第一劑az疫苗[會]有哪些副作用":
        # write your code here
        pass
    

    return resultDICT