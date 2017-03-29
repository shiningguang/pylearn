# coding=utf-8

age = int(raw_input("请问你几岁？"))
mail = raw_input("请问你性别是？（m表示男性，f表示女性）")
if mail == "f" and age >=10 and age <=12:
    print "恭喜你可以加入战队"
else:
    print "sorry，你不符合要求。不能加入足球队"