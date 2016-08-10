#coding=utf-8
import urllib    
import urllib2    
import json
import time
import MySQLdb
import datetime
import logging
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

  
url = 'http://10.25.24.51:10090/api/rest/nlp/SimRest/葡萄牙 成员国 彭博 西班牙 预算 罚款 进行/1.20802607966 1.13296544777 1.0252107077 0.973965301186 0.815128513269 0.790691585947 0.278559287551'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'    
 
headers = {
            'Referer':'http://finance.sina.com.cn/',
            'User-Agent': user_agent
            }

# 2 调用restful接口进行相似度计算
url_simTest = "http://10.25.24.51:10090/api/rest/nlp/matchscore/"
print url_simTest
post_data = {
    'keywordlist': str(str_keyword),
    'weightlist': str(str_weights),
}
data = urllib.urlencode(post_data)
req = urllib2.Request(
    url=url_simTest,
    data=post_data,
    headers=headers
)
result = urllib2.urlopen(req)
text = result.read()
# print text;
hjson_jieba = json.loads(text)
