import urllib2
import cookielib

# -------------
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
#
# response = opener.open('http://www.baidu.com')
#
# for item in cookie:
#     print item.name + ' : ' +item.value

# ---------------
# filename = "cookie.txt"
# cookie = cookielib.MozillaCookieJar(filename)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('http://www.baidu.com')
#
# cookie.save(ignore_discard=True,ignore_expires=True)


# filename = "cookie.txt"
# cookie = cookielib.MozillaCookieJar()
# cookie.load(filename, ignore_expires=True)
# req = urllib2.Request("http://www.baidu.com")
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
#
# print response.read()


