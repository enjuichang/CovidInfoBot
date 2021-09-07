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

DEBUG_group = True
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "dose": ["第一劑", "第三劑", "第二劑"], "doze": ["第一劑", "第二劑", "第三劑"], "Taiwan": ["全台", "全台灣", "全國", "全島", "全臺", "全臺各地", "全臺灣", "台灣", "本國", "本島", "臺灣"], "Medigen": ["Medigen", "medigen", "高端"], "Moderna": ["Moderna", "莫德納"], "leftover": ["剩量", "剩餘", "剩餘分佈", "剩餘分布", "剩餘數", "剩餘數字", "剩餘資料", "剩餘量","庫存"], "syn_verb": ["有", "出現"], "group_num": ["第一類", "第二類", "第三類", "第四類", "第五類", "第六類", "第七類", "第八類", "第九類", "第十類"], "side_effect": ["副作用", "嚴重副作用"], "vaccine_verb": ["注射", "接種", "打完", "打過"], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "上海復興", "上海復興BNT", "輝瑞"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_group:
        print("[group] {} ===> {}".format(inputSTR, utterance))

def groupnumber(args, userDefinedDICT, resultDICT, resultSTR): #避免有太多類別
    count=0
    if args in userDefinedDICT["group_num"]:
        if count == 0:
            resultDICT[resultSTR].append(args)
            count += 1
        if count > 0:
            print("太多類囉! 您想要哪一個?")
    else:
        pass

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["group_num"] = []
    if utterance == "[第一類][族群]":
        groupnumber(args[0], userDefinedDICT, resultDICT, "group_num")

    if utterance == "[第一類]接種[對象]":
        groupnumber(args[0], userDefinedDICT, resultDICT, "group_num")

    return resultDICT