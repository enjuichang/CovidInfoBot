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

DEBUG_side_effect = True
userDefinedDICT = {"AZ": ["AstraZeneca", "az", "AZ", "牛津/阿斯利康", "牛津", "阿斯利康", "阿斯特捷利康"], "doze": ["第一劑", "第二劑", "第三劑"], "Moderna": ["Moderna", "莫德納"], "syn_verb": ["有", "出現"], "side_effect": ["副作用", "嚴重副作用"], "vaccine_verb": ["注射", "接種", "打完", "打過"], "Pfizer-BioNTech": ["Pfizer-BioNTech", "輝瑞", "BNT", "Biotech", "BioTech", "biotech", "BIOTECH"]}
vaccinedict = userDefinedDICT["AZ"] + userDefinedDICT["Moderna"] + userDefinedDICT["Pfizer-BioNTech"]
vaccinedict = vaccinedict + ["AstraZeneca", "Moderna", "Pfizer-BioNTech"]
# 將符合句型的參數列表印出。這是 debug 或是開發用的。

with open("intent/side_effect.json", mode="r", encoding="utf-8") as file:
    sideeffectDict = json.loads(file.read())

with open("intent/hospital_immediately.json", mode="r", encoding="utf-8") as f:
    hospitaldict = json.loads(f.read())

def debugInfo(inputSTR, utterance):
    if DEBUG_side_effect:
        print("[side_effect] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["疫苗"] = []
    resultDICT["副作用"] = []
    resultDICT["嚴重副作用"] = []
    if utterance == "[az][疫苗]副作用為何":
        if args[0] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["副作用"].append(sideeffectDict[k])

    if utterance == "[az]副作用":
        if args[0] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["副作用"].append(sideeffectDict[k])

    if utterance == "[az]疫苗[會]有哪些副作用":
        if args[0] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["副作用"].append(sideeffectDict[k])

    if utterance == "[打完][莫德納][後]，[出現]哪些嚴重副作用需要送醫": #嚴重副作用
        if args[1] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["嚴重副作用"].append(hospitaldict[k])

    if utterance == "[打完][莫德納]疫苗[後]，[出現]哪些嚴重副作用需要送醫": #嚴重副作用
        if args[1] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["嚴重副作用"].append(hospitaldict[k])

    if utterance == "[第一劑][az][會]有哪些副作用":
        if args[1] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["副作用"].append(sideeffectDict[k])

    if utterance == "[第一劑][az]副作用":
        if args[1] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["副作用"].append(sideeffectDict[k])

    if utterance == "[第一劑][az]疫苗[會]有哪些副作用":
        if args[1] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["副作用"].append(sideeffectDict[k])

    if utterance == "[第一劑][az]疫苗副作用":
        if args[1] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["副作用"].append(sideeffectDict[k])

    if utterance == "請問[az]疫苗副作用為何":
        if args[0] in vaccinedict:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["疫苗"].append(k)
                    resultDICT["副作用"].append(sideeffectDict[k])

    return resultDICT