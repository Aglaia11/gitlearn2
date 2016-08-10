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

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
 
headers = {
            'Referer':'http://finance.sina.com.cn/',
            'User-Agent': user_agent
            }
str_keyword="上海 南京"
str_weights="0.1 0.2"
# 2 调用restful接口进行相似度计算
url_simTest = "http://10.25.24.51:10090/api/rest/nlp/matchscore"
print url_simTest
post_data = {
    'keywordlist': str_keyword,
    'weightlist': str_weights,
}
data = urllib.urlencode(post_data)
req = urllib2.Request(
    url=url_simTest,
    data=data,
    headers=headers
)
result = urllib2.urlopen(req)
text = result.read()
# print text;
hjson_jieba = json.loads(text)
