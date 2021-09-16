#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for group

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    Output:
        resultDICT    dict
"""
import json
DEBUG_group = True
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "blank": [""], "Taiwan": ["全台", "全台灣", "全國", "全島", "全臺", "全臺各地", "全臺灣", "台灣", "本國", "本島", "臺灣"], "Medigen": ["Medigen", "medigen", "高端"], "Moderna": ["Moderna", "莫德納"], "leftover": ["剩量", "剩餘", "剩餘分佈", "剩餘分布", "剩餘數", "剩餘數字", "剩餘資料", "剩餘量"], "syn_verb": ["有", "出現"], "group_num": ["第一類", "第二類", "第三類", "第四類", "第五類", "第六類", "第七類", "第八類", "第九類", "第十類"], "第一劑": ["第 1 劑", "第1劑", "第 1劑", "第1 劑", "第１劑"], "第二劑": ["第 2 劑", "第2劑", "第 2劑", "第2 劑", "第２劑"], "information": [""], "side_effect": ["副作用"], "updated_info": [""], "vaccine_verb": [""], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "上海復興", "上海復興BNT", "輝瑞", "bnt"]}
with open("json/group_num.json", mode="r", encoding="utf-8") as file:
    groupDICT = json.loads(file.read())

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_group:
        print("[group] {} ===> {}".format(inputSTR, utterance))

def groupnumber(args, resultDICT, resultSTR, resultSTR2): #避免有太多類別
    count=0
    if args in userDefinedDICT["group_num"]:
        if count == 0:
            resultDICT[resultSTR].append(args)
            group_num_def = groupDICT[args]
            resultDICT[resultSTR2].append(group_num_def)
            count += 1
        if count > 0:
            print("太多類囉! 您想要哪一個?")
    else:
        pass

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["group_num"] = []
    
    if utterance == "[第一類]對象":
        groupnumber(args[0], resultDICT, "group_num","group_num_def")

    if utterance == "[第一類]接種對象":
        # write your code here
        pass

    if utterance == "[第一類]接種族群":
        # write your code here
        pass

    if utterance == "[第一類]族群":
        # write your code here
        pass

    return resultDICT