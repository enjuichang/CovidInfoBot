#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging #可以測試哪裡有問題
import discord
import json
import re
from covid_info_bot import runLoki

import response_parser
from pprint import pprint


logging.basicConfig(level=logging.CRITICAL)

# <取得多輪對話資訊>
client = discord.Client()

sideEffectTemplate ={
                "vaccine_shot":"",
                 "side_effect": "",
                 }

vaccineStockTemplate = {
                "vaccine_shot":"",
                "vaccine_stock":""
                    }

mscDICT = {
    # "userID": {side_effectTemplate, vaccine_stockTemplate}
}
# </取得多輪對話資訊>

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
# 另一個寫法是：accountDICT = json.load(open("account.info", encoding="utf-8"))


punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT



@client.event
async def on_ready():
    logging.info("[READY INFO] {} has connected to Discord!".format(client.user))
    print("[READY INFO] {} has connected to Discord!".format(client.user))


@client.event
async def on_message(message):
    if message.channel.name != "bot_test":
        return

    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return

    try:
        print("client.user.id =", client.user.id, "\nmessage.content =", message.content)
        msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
        print("msgSTR =", msgSTR)
        replySTR = ""    # Bot 回應訊息

        if re.search("(hi|hello|哈囉|嗨|[你您]好)", msgSTR.lower()):
            replySTR = "Hi 您好，想知道哪些疫苗資訊呢?"
            await message.reply(replySTR)
            return

        lokiResultDICT = getLokiResult(msgSTR)    # 取得 Loki 回傳結果

        if lokiResultDICT:
            if client.user.id not in mscDICT:    # 判斷 User 是否為第一輪對話
                mscDICT[client.user.id] = { 
                                            # "vaccine_shot" : {},
                                            "side_effect": {},
                                           "vaccine_stock": {},
                                        #    "loan_type": "side_effect",
                                           "completed": False}

            for k in lokiResultDICT:    # 將 Loki Intent 的結果，存進 Global mscDICT 變數，可替換成 Database。
                if k == "side_effect":
                    for c in lokiResultDICT["side_effect"]:
                        mscDICT[client.user.id]["side_effect"][c] = lokiResultDICT["side_effect"][c]
                        mscDICT[client.user.id]["vaccine_stock"][c] = lokiResultDICT["side_effect"][c]
                elif k == "vaccine_stock":
                    for m in lokiResultDICT["vaccine_stock"]:
                        mscDICT[client.user.id]["vaccine_stock"][m] = lokiResultDICT["vaccine_stock"][m]
                # elif k == "msg":
                #     replySTR = lokiResultDICT[k]
                #     if "loan_type" in lokiResultDICT:
                #         mscDICT[client.user.id]["loan_type"] = lokiResultDICT["loan_type"]
                #     if mscDICT[client.user.id]["side_effect"] == {} and mscDICT[client.user.id]["vaccine_stock"] == {}:
                #         replySTR += "\n請問您從事什麼工作呢？"
                #     print("Loki msg:", replySTR, "\n")
                elif k == "confirm":
                    if lokiResultDICT["confirm"]:
                        replySTR = "好的，謝謝。"
                    else:
                        replySTR = "請問您的意思是？"

            if mscDICT[client.user.id]["loan_type"] == "side_effect" and replySTR == "":    # side_effect 多輪對話的問句。
                if "vaccine_shot" not in mscDICT[client.user.id]["side_effect"]:
                    replySTR = "請問要詢問哪隻疫苗呢？"
                elif "side_effect" not in mscDICT[client.user.id]["side_effect"]:
                    replySTR = "請問要問關於{}疫苗的甚麼資訊呢?".format(mscDICT[client.user.id]["side_effect"]["vaccine_shot"])
                # elif "annual_income" not in mscDICT[client.user.id]["side_effect"]:
                #     replySTR = "請問您個人的年收入大概是多少呢？"
                # elif "education" not in mscDICT[client.user.id]["side_effect"]:
                #     replySTR = "請問您的教育程度是？"

            if set(sideEffectTemplate.keys()).difference(mscDICT[client.user.id]["side_effect"]) == set() and mscDICT[client.user.id]["loan_type"] == "side_effect":
                replySTR = """感謝您的幫忙。和您確認以下個人信貸的申請資料…
                              您從事的是 [{}]，已經有 [{}] 的經驗了，目前年收入約 [{}] 元。
                              如果以上正確的話，我們將在這兩天內與您聯絡。""".format(mscDICT[client.user.id]["side_effect"]["job"],
                                                                                     mscDICT[client.user.id]["side_effect"]["job_year"],
                                                                                     mscDICT[client.user.id]["side_effect"]["annual_income"]).replace("    ", "")
                mscDICT[client.user.id]["completed"] = True

            if mscDICT[client.user.id]["loan_type"] == "vaccine_stock" and replySTR == "":    # vaccine_stock 多輪對話的問句。
                if "job" not in mscDICT[client.user.id]["vaccine_stock"]:
                    replySTR = "請問您從事什麼工作呢？"
                elif "job_year" not in mscDICT[client.user.id]["vaccine_stock"]:
                    replySTR = "請問您從事 [{}] 多久了呢？".format(mscDICT[client.user.id]["vaccine_stock"]["job"])
                elif "annual_income" not in mscDICT[client.user.id]["vaccine_stock"]:
                    replySTR = "請問您個人的年收入大概是多少呢？"
                elif "education" not in mscDICT[client.user.id]["vaccine_stock"]:
                    replySTR = "請問您的教育程度是？"
                elif "address" not in mscDICT[client.user.id]["vaccine_stock"]:
                    replySTR = "請問您的地址是？"
                elif "floor_size" not in mscDICT[client.user.id]["vaccine_stock"]:
                    replySTR = "請問房屋的坪數是？"
                elif "year" not in mscDICT[client.user.id]["vaccine_stock"]:
                    replySTR = "請問屋齡是幾年？"
                elif "type" not in mscDICT[client.user.id]["vaccine_stock"]:
                    replySTR = "請問您的房屋的類型是？"

            if set(vaccineStockTemplate.keys()).difference(mscDICT[client.user.id]["vaccine_stock"]) == set() and mscDICT[client.user.id]["loan_type"] == "vaccine_stock":
                replySTR = """感謝您的幫忙。和您確認以下個人房貸的申請資料…
                              您從事的是 [{}]，已經有 [{}] 的經驗了，目前年收入約 [{}] 元;
                              房屋的地址是 [{}]、坪數為 [{}]，屋齡是 [{}]，房屋的類型是 [{}]。
                              如果以上正確的話，我們將在這兩天內與您聯絡。""".format(mscDICT[client.user.id]["vaccine_stock"]["job"],
                                                                                     mscDICT[client.user.id]["vaccine_stock"]["job_year"],
                                                                                     mscDICT[client.user.id]["vaccine_stock"]["annual_income"],
                                                                                     mscDICT[client.user.id]["vaccine_stock"]["address"],
                                                                                     mscDICT[client.user.id]["vaccine_stock"]["floor_size"],
                                                                                     mscDICT[client.user.id]["vaccine_stock"]["year"],
                                                                                     mscDICT[client.user.id]["vaccine_stock"]["type"]).replace("    ", "")
                mscDICT[client.user.id]["completed"] = True

        print("mscDICT =")
        pprint(mscDICT)

        if mscDICT[client.user.id]["completed"]:    # 清空 User Dict
            del mscDICT[client.user.id]

        if replySTR:    # 回應 User 訊息
            await message.reply(replySTR)
        return

    except Exception as e:
        logging.error("[MSG ERROR] {}".format(str(e)))
        print("[MSG ERROR] {}".format(str(e)))





if __name__ == "__main__":
    client.run(accountDICT["discord_token"])

    #getLokiResult("我想辦房屋貸款，我是一位會計師")