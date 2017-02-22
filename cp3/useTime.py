# coding=utf-8


distance = 200.0
velocity = 80.0

usetime = distance/velocity
h = usetime - usetime%1
m = (usetime-h)*60  - (usetime-h)*60%1

print "需要",h,"小时",m,"分钟"
