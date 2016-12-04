# coding=utf-8
__author__ = 'chenshuguang'

# 测试正则表达式

# 导入re模块
import re

# 将正则表达式编译成pattern对象，注意hello前的r意思是原生字符串

pattern = re.compile(r'hello')

r1 = re.match(pattern, 'hello')
r2 = re.match(pattern, 'helloC')
r3 = re.match(pattern, 'helo')
r4 = re.match(pattern, 'helloo Chenshuguang')

if r1:
    print r1.group()
else:
    print 'r1匹配失败'


if r2:
    print r2.group()
else:
    print 'r2匹配失败'

if r3:
    print r3.group()
else:
    print 'r3匹配失败'

if r4:
    print r4.group()
else:
    print 'r4匹配失败'