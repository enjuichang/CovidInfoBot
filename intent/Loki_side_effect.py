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
    sideeffectDICT = json.loads(file.read())

with open("json/hospital_immediately.json", mode="r", encoding="utf-8") as f:
    hospitalDICT = json.loads(f.read())

DEBUG_side_effect = True
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "Taiwan": ["全台", "全台灣", "全國", "全島", "全臺", "全臺各地", "全臺灣", "台灣", "本國", "本島", "臺灣"], "severe": ["嚴重"], "Medigen": ["Medigen", "medigen", "高端"], "Moderna": ["Moderna", "莫德納"], "leftover": ["剩量", "剩餘", "剩餘分佈", "剩餘分布", "剩餘數", "剩餘數字", "剩餘資料", "剩餘量"], "syn_verb": ["有", "出現"], "group_num": ["第一類", "第二類", "第三類", "第四類", "第五類", "第六類", "第七類", "第八類", "第九類", "第十類"], "第一劑": ["第 1 劑", "第1劑", "第 1劑", "第1 劑", "第１劑"], "第二劑": ["第 2 劑", "第2劑", "第 2劑", "第2 劑", "第２劑"], "information": ["資訊", "最新資訊"], "side_effect": ["副作用"], "updated_info": ["最新", "目前"], "vaccine_verb": ["注射", "接種", "打完", "打過"], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "上海復興", "上海復興BNT", "輝瑞", "bnt"]}
vaccineDICT = userDefinedDICT["AZ"] + userDefinedDICT["Moderna"] + userDefinedDICT["Pfizer-BioNTech"] + userDefinedDICT["Medigen"]

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_side_effect:
        print("[side_effect] {} ===> {}".format(inputSTR, utterance))

def formalize_name_side_effect(val, resultDICT, resultSTR, resultSTR2):
    count = 0
    for k in userDefinedDICT.keys():
        if val in userDefinedDICT[k]:
            if count == 0: 
                resultDICT[resultSTR].append(k)
                side_effect = sideeffectDICT[k]
                resultDICT[resultSTR2].append(side_effect)
                resultDICT["inquiry_type"].append("side_effect")
                count+=1
            if count > 1: 
                print(f"Name Error: Duplicate Names! ({val})")

def formalize_name_severe_side_effect(val, resultDICT, resultSTR, resultSTR2):
    count = 0
    for k in userDefinedDICT.keys():
        if val in userDefinedDICT[k]:
            if count == 0: 
                resultDICT[resultSTR].append(k)
                severe_side_effect= hospitalDICT[k]
                resultDICT[resultSTR2].append(severe_side_effect)
                resultDICT["inquiry_type"].append("severe_side_effect")
                count+=1
            if count > 1: 
                print(f"Name Error: Duplicate Names! ({val})")

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if resultDICT == {}:
        resultDICT["vaccine_shot"] = []
        resultDICT["side_effect"] = []
        resultDICT["severe_side_effect"] = []
        resultDICT["inquiry_type"] = []

    if utterance == "[az][嚴重]副作用":
        if args[1] in userDefinedDICT["severe"]:
            formalize_name_severe_side_effect(args[0], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[1] == []:
            formalize_name_side_effect(args[0], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[az]疫苗[嚴重]副作用":
        if args[1] in userDefinedDICT["severe"]:
            formalize_name_severe_side_effect(args[0], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[1] == []:
            formalize_name_side_effect(args[0], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[打完][莫德納][後]，[出現]哪些[嚴重]副作用需要送醫":
        if args[4] in userDefinedDICT["severe"]:
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[4] == []:
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[打完][莫德納]疫苗[後]，[出現]哪些[嚴重]副作用需要送醫":
        if args[4] in userDefinedDICT["severe"]:
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[4] == []:
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[第一劑][az][嚴重]副作用":
        if args[2] in userDefinedDICT["severe"]:
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[2] == []:
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[第一劑][az][會][有]哪些[嚴重]副作用":
        if args[4] in userDefinedDICT["severe"]:
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[4] == []:
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[第一劑][az]疫苗[嚴重]副作用":
        if args[2] in userDefinedDICT["severe"]:
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[2] == []:
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[第一劑][az]疫苗[會][有]哪些[嚴重]副作用":
        if args[4] in userDefinedDICT["severe"]:
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[4] == []:
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "請問[az]疫苗[嚴重]副作用為何":
        if args[1] in userDefinedDICT["severe"]:
            formalize_name_severe_side_effect(args[0], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[1] == []:
            formalize_name_side_effect(args[0], resultDICT, "vaccine_shot", "side_effect")
            
    resultDICT["side_effect_var"] = []
    return resultDICT