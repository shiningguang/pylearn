# coding=utf-8

total = raw_input("请输入总价：")
tip = raw_input("小费：")
sumperson = raw_input("人数：")
sumpersonI = int(sumperson)
totalF = float(total)
tipF = float(tip)

perPay = totalF * (1+tipF) / sumpersonI


print "每个人需要付",perPay
