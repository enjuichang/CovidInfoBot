import urllib.request as req
from bs4 import BeautifulSoup
import json
from pprint import pprint
import bs4

url= "https://www.dpp.org.tw/media/contents/9178" #這邊需要再改(希望可以把url裝在list中，然後就可以一一讀取網頁資訊)

def get2021dppdata(url):
    #print(url)
    request = req.Request(url, headers={
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)
    root = bs4.BeautifulSoup(data, "html.parser")
    #print(root)
    contents = root.find_all("div", class_="w80 container")
    for content in contents:
        full_text = content.getText()
        
    full_text = full_text.replace("\n","").replace("\r\n","").replace("\t","").replace("\t\xa0\n","")
    with open("dpp2021fed.txt", mode="w", encoding="utf-8") as f:
        f.write(full_text)

# get2021dppdata(url)

url = "http://www.kmt.org.tw/2020/08/blog-post_18.html"

def get2021kmtdata(url):
    request = req.Request(url, headers={
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    #print(data)
    root = bs4.BeautifulSoup(data, "html.parser")
    contents = root.find_all("div", class_="post-body entry-content inpost")
    # eng_contents = root.find_all("span", class_="") #想要把英文部分擷取出來後，利用replace把英文稿去除，最後只留下中文稿 (但未成功)
    for content in contents:
        kmt_full_text = content.getText()
    # for eng_content in eng_contents:
    #     kmt_eng_full_text = eng_content.getText()
    
    # return print(data)
    # return print(kmt_eng_full_text)
    with open("kmt2021fed.txt", mode="w", encoding="utf-8") as f:
        f.write(kmt_full_text)
    
    # with open("kmt2021fed.json", mode="w", encoding="utf-8") as f: #不確定是否要寫進json檔中，還是只要寫在txt檔中就可以了
    #     json.dump(kmt_full_text, f)
    
    return print(kmt_full_text)

url = "https://www.ftvnews.com.tw/news/detail/2021510P12M1"
def getftvdata(url):
    request = req.Request(url, headers={
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)
    root = bs4.BeautifulSoup(data, "html.parser")
    contents = root.find_all("div", id="newscontent")
    contents1 = root.find_all("div", id="preface")
    for content1 in contents1:
        ftv_full_text1 = content1.getText()
    # print(ftv_full_text1)
    for content in contents:
        ftv_full_text = content.getText()
    # print(ftv_full_text)
    total_full_text = ftv_full_text1 + ftv_full_text
    with open("ftv2021fed.txt", mode="w", encoding="utf-8") as f:
        f.write(total_full_text)
    return print(total_full_text)

getftvdata(url)