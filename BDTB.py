# coding=utf-8
# 爬取百度贴吧内容

import urllib2
import re

class Tool:

    # 去除img标签
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除a标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签替换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 把表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n 加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行替换为\n
    repaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n      ",x)
        x = re.sub(self.repaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)

        return x.strip()

# 百度贴吧爬虫
class BDTB:

    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseurl, seeLZ, floorTag):
        self.baseURL = baseurl
        self.seeLZ = '?see_LZ='+str(seeLZ)
        # html标签剔除工具
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaultTitle = u"百度贴吧"
        self.floorTag = floorTag


    # 获取一页的数据
    def getPage(self, pageNum):
        try:
            url = self.baseURL+self.seeLZ + '&pn=' + str(pageNum)
            print url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"链接百度贴吧失败",e.reason
                return None

    # 获取贴吧的标题
    def getTitle(self, page):
        pattern = re.compile('<h3 class="core_title_txt.*?">(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None


    # 获取页数
    def getPageNum(self, page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # 获取内容
    def getContext(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = '\n' + self.tool.replace(item)+'\n'
            contents.append(content.encode('utf-8'))
        return contents


    def setFileTitle(self,title):
        if title is not None:
            self.file = open(title+".txt","w+")
        else:
            self.file = open(self.defaultTitle+".txt","w+")

    def writeData(self,contents):
        for item in contents:
            if self.floorTag == "1":
                floorLine = "\n" +str(self.floor)+ u"------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor +=1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URL已失效，请重试"
            return
        try:
            print "该帖子有" + str(pageNum) +"页"
            for i in range(1, int(pageNum)+1):
                print "正在写入第"+str(i) +"页数据"
                page = self.getPage(i)
                contents = self.getContext(page)
                self.writeData(contents)
        except IOError,e:
            print "写入异常，原因" + e.message
        finally:
            print "写入完成"

print u"请输入帖子代号"
baseURL = 'http://tieba.baidu.com/p/' +str(raw_input(u"http://tieba.baidu.com/p/"))
seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0 \n")
floorTag = raw_input("是否写入楼层信息，是输入1，否输入0 \n")
bdtb = BDTB(baseURL,seeLZ,floorTag)
bdtb.start()






