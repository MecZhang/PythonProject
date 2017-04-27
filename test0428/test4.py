# _*_ coding:utf-8 _*_ 
# 利用requests库抓取贴吧中的网友，并保存到本地

import requests
def baidu_tieba(url,pages_list):
    r = requests.get(url)
    resp = r.json()
#未完待续
    
    
    
if __name__ == "__main__":
    url = "http://tiebai.baidu.com/p/"
    pages_list = [4779995461, 4781463980, 4826066853, 4560596856, 4819859278]
    baidu_tieba(url, pages_list)
