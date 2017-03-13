# coding=utf-8

long = int(raw_input("输入房间长："))
width = int(raw_input("请输入房间宽："))

area = long * width

price = int(raw_input("请输入每块毯子的价格："))


print "需要",area,"块毯子",",毯子是每平米","总价是：",price * area
print "需要",area * 9,"块毯子",",毯子是每平方尺","总价是：",price * area * 9

