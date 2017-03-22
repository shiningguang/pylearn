# coding=utf-8

import easygui

firstname = easygui.enterbox("请输入你的名字")
housenum = easygui.enterbox("请输入你的房间号")
street = easygui.enterbox("请输入你的街道")
city = easygui.enterbox("请输入你的城市")
province = easygui.enterbox("请输入你的省份")
zipcode = easygui.enterbox("请输入你的邮编")

easygui.msgbox(firstname+"\n"+housenum+" "+street+" "+city+" "+province+"\n"+zipcode)

