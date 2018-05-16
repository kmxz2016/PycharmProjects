import urllib.request
import ssl
import re
import os

def writeFileBytes(htmlBytes,toPath):
    with open(toPath,"wb") as f:
        f.write(htmlBytes)
def writeFileStr(htmlBytes,toPath):
    with open(toPath,"w") as f:
        f.write(str(htmlBytes))
def getHtmlBytes(url):
    headers = {"User-Agent":"Mozilla/5.0(Winsows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/59.0.33071.115 Safari/537.36"}
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    return response.read()
def qqCrawler(url,toPath):
    htmlBytes = getHtmlBytes(url)
    # writeFileBytes(htmlBytes,r"/home/km/PycharmProjects/爬虫/file1.html")
    # writeFileStr(htmlBytes,r"/home/km/PycharmProjects/爬虫/file2.txtl")
    htmlStr = str(htmlBytes)
    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat)
    qqsList= re_qq.findall(htmlStr)
    qqsList=list(set(qqsList))
    print(qqsList)
    print(len(qqsList))
url = "https://www.douban.com/group/topic/17359302/"
toPath = r"/home/km/PycharmProjects/爬虫/qqfile.txt"
qqCrawler(url,toPath)