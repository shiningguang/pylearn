# coding=utf-8

fivecents = int(raw_input("有几个五分币："))
twocents = int(raw_input("有几个二分币："))
cents = int(raw_input("有几个一分币："))

totalCents = (fivecents * 5.0 + twocents * 2.0 + cents)/100

print "总共有：" ,totalCents,"元"