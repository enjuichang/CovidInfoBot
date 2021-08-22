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

DEBUG_side_effect = True
userDefinedDICT = {"AZ": ["AstraZeneca", "az", "AZ", "牛津/阿斯利康", "牛津", "阿斯利康", "阿斯特捷利康"], "doze": ["第一劑", "第二劑", "第三劑"], "Moderna": ["Moderna", "莫德納", "莫德納疫苗"], "side_effect": ["副作用"], "Pfizer-BioNTech": ["Pfizer-BioNTech", "輝瑞", "輝瑞疫苗", "BNT", "Biotech", "BioTech", "biotech", "BIOTECH"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_side_effect:
        print("[side_effect] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[az][疫苗]副作用為何":
        # write your code here
        pass

    if utterance == "[az]副作用":
        # write your code here
        pass

    if utterance == "[az]疫苗[會]有哪些副作用":
        # write your code here
        pass

    if utterance == "[第一劑][az][疫苗][會]有哪些副作用":
        # write your code here
        pass

    if utterance == "[第一劑][az][疫苗]副作用":
        # write your code here
        pass

    if utterance == "請問[az]疫苗副作用為何":
        # write your code here
        pass

    return resultDICT