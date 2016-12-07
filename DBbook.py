# coding=utf-8
# 爬取豆瓣读书用于生产物料
import os
import re
import urllib2
import urllib
import uuid

import MySQLdb
import sys
from bs4 import BeautifulSoup


conn = MySQLdb.Connect(
                    host = '127.0.0.1',
                    port = 3306,
                    user = 'root',
                    passwd = 'root',
                    db = 'spider',
                    charset = 'utf8'
    )

reload(sys)
sys.setdefaultencoding('utf-8')


class DBBOOK:

    # 传入豆瓣读书top250的url:https://book.douban.com/top250
    def __init__(self,url):
        self.url = url
        self.imgpath = "/opt/var/doubanbook/"

    # 网络请求，获取html
    def getPage(self):
        try:
            url = self.url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"豆瓣链接失效",e.reason
                return None

    # 请求页面提取数据
    def getContent(self,page):
        soup = BeautifulSoup(page)
        self.url = soup.find('span',attrs={'class':'thispage'}).find_next('a').get('href')
        pattern = re.compile(r'https:*?')
        match = pattern.match(self.url)
        if not match:
            self.url = None
        contents = soup.find_all('table', width="100%")

        for i in range(0, len(contents)):
            content = str(contents[i])
            item = BeautifulSoup(content)
            img = item.find('img').get('src')

            id = item.find('a', attrs={'class': 'nbg'}).get('href')
            id = id.strip().decode('utf8')
            title = item.find('div', attrs={'class': 'pl2'}).find('a').get_text()
            title = title.strip()
            title = title.decode('utf8')
            auth = item.find('p', attrs={'class': 'pl'}).get_text()
            auth = auth.strip()
            auth = auth.decode('utf8')
            con = item.find('span', attrs={'class': 'inq'}).get_text()
            con = con.strip()
            con = con.decode('utf8')
            try:
                print img
                imgData = urllib2.urlopen(img).read()
                id = str(uuid.uuid1())
                fileName = self.imgpath + id +".jpg"
                output = open(fileName, 'wb+')
                output.write(imgData)
                output.close()
                print u"保存图片成功"

            except Exception, e:
                print e
                print u"保存图片出错"



            imgpath = str(self.imgpath)+str(id)

            sql_insert = 'insert into doubandushu (id,title,author,content,imgurl) VALUES ("'\
                         + str(id) + '","' + title + '","' + auth + '","' + con + '","' + imgpath + '")'
            cursor = conn.cursor()
            try:
                cursor.execute(sql_insert)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
            cursor.close()







    def getBookImg(self, url):
        try:
            req = urllib2.Request(url)
            operate = open(req)
            data = operate.read()
            return data
        except Exception,e:
            print e
            return None


    def saveBookImg(self,path,img_name,data):
        if data == None:
            return
        file  = open(path+img_name+'.jpg', "wb")
        file.write(data)
        file.flush()
        file.close()

        return path+img_name



    def insertBookinfoToMysql(self,id,title,author,content,bookimg):
        sql_insert = 'insert into doubandushu (id,title,author,content,imgurl) VALUES ('+id+','+title+','+author+','+content+','+bookimg+')'
        cursor = conn.cursor()
        try:
            cursor.execute(sql_insert)
            conn.commit()
        except Exception as e:
            print e
            conn.rollback()
        cursor.close()







baseUrl='https://book.douban.com/top250'
db = DBBOOK(baseUrl)
while db.url != None:
    page = db.getPage()
    db.getContent(page)

conn.close()
# soup = BeautifulSoup(db.getPage())
# print soup.prettify()
# print soup.find('span',attrs={'class':'thispage'}).find_next('a').get('href')
# contents = soup.find_all('table', width="100%")
#
# for i in range(0, len(contents)):
#     content = str(contents[i])
#     item = BeautifulSoup(content)
#     # item = BeautifulSoup(contents[i])
#     # item.strings()
#     img = item.find('img').get('src')
#     print img.strip()
#     id = item.find('a',attrs={'class':'nbg'}).get('href')
#     print id.strip()
#     title = item.find('div', attrs={'class':'pl2'}).find('a').get_text()
#     print title.strip()
#     auth = item.find('p',attrs={'class':'pl'}).get_text()
#     print auth.strip()
#     con = item.find('span',attrs={'class':'inq'}).get_text()
#     print con.strip()
