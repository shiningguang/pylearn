# coding=utf-8

import easygui

f = easygui.enterbox("请输入华氏温度度数：")
f = float(f)
c = 5 * (f - 32) / 9

easygui.msgbox("温度是：" + str(c))

