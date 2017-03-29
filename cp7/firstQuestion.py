# coding=utf-8

price = int(raw_input("请输入价格："))

if price <= 10 :
    print "价格是",price*0.1,"打一折"
else:
    print "价格是",price*0.2,"打二折"


