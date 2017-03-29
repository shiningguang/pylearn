# coding=utf-8

rest = 200
v = int(raw_input("请输入邮箱多大？"))
percent = float(raw_input("请问邮箱有多满？按100输入就是全满"))/100
speed = float(raw_input("请问你汽车每升油行驶多长距离？单位千米"))

s = (v-5)*percent*speed


if s > rest:
    print "你可以到下一个加油站加油"
else:
    print "你必须在这个加油站加油"


