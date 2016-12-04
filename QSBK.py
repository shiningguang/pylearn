# coding=utf-8
# 爬取糗事百科热门

import urllib2
import re

class QSBK:

    # 初始化方法

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        self.headers = {'User-Agent' : self.user_agent }

        # 存放段子的变量
        self.stories = []
        # 存放段子是否继续运行的变量
        self.enable = False


    def getPage(self,pageIndex ):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
            # pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
        except urllib2.URLError ,e :
            if hasattr(e, "reason"):
                print u"连接糗事百科失败,错误原因", e.reason
                return None



    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败...."
            return None
        pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)

        items = re.findall(pattern, pageCode)

        return  items

    def loadPage(self):
        if self.enable == True:
            if len(self.stories ) <2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1


    def getOneStory(self,pageStories,page):
        for story  in pageStories:
            input = raw_input()
            self.loadPage()

            if input == 'Q':
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t赞:%s\n%s\n" %(page,story[0],story[2],story[1])

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable :
            if len(self.stories) >0 :
                pageStories = self.stories[0]
                nowPage+=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)


spider = QSBK()
spider.start()
