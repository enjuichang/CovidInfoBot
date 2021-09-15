#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Probe

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Probe = True
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "dose": ["第一劑", "第三劑", "第二劑"], "Taiwan": ["全台", "全台灣", "全國", "全島", "全臺", "全臺各地", "全臺灣", "台灣", "本國", "本島", "臺灣"], "Medigen": ["Medigen", "medigen", "高端"], "Moderna": ["Moderna", "莫德納"], "leftover": ["剩量", "剩餘", "剩餘分佈", "剩餘分布", "剩餘情形", "剩餘數", "剩餘數字", "剩餘狀況", "剩餘資料", "剩餘量", "庫存"], "location": ["台北", "台北市", "臺北", "北市", "臺北市", "天龍", "天龍國", "Taipei", "taipei", "Taipei City", "Taibei", "Taibei City", "TPE", "tpe", "taipei city", "taibei city", "新北", "新北市", "台北縣", "臺北縣", "New Taipei City", "new taipei city", "New Taipei", "new taipei", "Xinbei City", "Xinbei", "xinbei city", "xinbei", "桃園", "桃園市", "桃市", "桃園縣", "Taoyuan City", "taoyuan city", "Taoyuan", "taoyuan", "Taoyuan County", "taoyuan county", "台中", "台中市", "臺中", "臺中市", "中市", "台中縣", "臺中縣", "Taichung City", "taichung city", "Taichung", "taichung", "Taichung County", "taichung county", "台南", "台南市", "臺南", "臺南市", "南市", "台南縣", "臺南縣", "Tainan City", "tainan city", "Tainan", "tainan", "Tainan County", "tainan county", "高雄", "高雄市", "高市", "高雄縣", "Kaohsiung City", "kaohsiung city", "Kaohsiung", "kaohsiung", "Kaohsiung County", "kaohsiung county", "新竹縣", "竹縣", "Hsinchu County", "hsinchu county", "彰化", "彰縣", "彰化縣", "Changhua County", "changhua county", "Changhua", "changhua", "雲林", "雲縣", "雲林縣", "Yunlin County", "yunlin county", "Yunlin", "yunlin", "屏東", "屏東縣", "Pingtung County", "pingtung county", "Pingtung", "pingtung", "基隆", "基隆市", "Keelung City", "keelung city", "Keelung", "keelung", "宜蘭", "宜蘭縣", "Ilan County", "ilan county", "Ilan", "ilan", "新竹", "新竹市", "竹市", "Hsinchu City", "hsinchu city", "Hsinchu", "hsinchu", "苗栗", "苗栗縣", "Miaoli County", "miaoli county", "Miaoli", "miaoli", "嘉義", "嘉義市", "嘉市", "Chiayi City", "chiayi city", "Chiayi", "chiayi", "嘉義縣", "嘉縣", "Chiayi County", "chiayi county", "花蓮", "花蓮縣", "Hualian County", "hualian county", "Hualian", "hualian", "臺東", "台東", "臺東縣", "台東縣", "Taitung County", "taitung county", "Taitung", "taitung", "南投", "南投縣", "Nantou County", "nantou county", "Nantou", "nantou", "澎湖", "澎湖縣", "Penghu County", "penghu county", "Penghu", "penghu", "Pescadores", "pescadores", "Pescadores Islands", "pescadores islands", "金門", "金門縣", "Kinmen County", "kinmen county", "Kinmen", "kinmen", "Quemoy Island", "quemoy island", "Quemoy", "quemoy", "連江", "馬祖", "馬祖列島", "馬祖列嶼", "連江縣", "Lianjiang County", "lianjiang county", "Lianjiang", "lianjiang", "Matsu Islands", "matsu islands", "Matsu", "Mazu", "matsu", "mazu"], "syn_verb": ["出現", "有"], "group_num": ["第一類", "第七類", "第三類", "第九類", "第二類", "第五類", "第八類", "第六類", "第十類", "第四類"], "第一劑": ["第 1 劑", "第 1劑", "第1 劑", "第1劑", "第１劑"], "第二劑": ["第 2 劑", "第 2劑", "第2 劑", "第2劑", "第２劑"], "information": ["最新資訊", "資訊"], "side_effect": ["副作用"], "updated_info": ["最新", "目前"], "vaccine_verb": ["打完", "打過", "接種", "注射"], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "bnt", "上海復興", "上海復興BNT", "輝瑞"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Probe:
        print("[Probe] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    # resultDICT["inquiry_type"] = []

    if utterance == "[我]想要知道疫苗[資訊]":
        resultDICT["msg"] = "想知道關於疫苗的哪些資訊呢? 如: 疫苗剩餘量、疫苗庫存量、疫苗副作用...等資訊"
    
    if utterance == "[我]想要知道[最新]疫苗資訊":
        resultDICT["msg"] = "想知道哪些最新疫苗資訊呢?"

    return resultDICT 