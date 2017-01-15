# coding=utf-8

import random

secret = random.randint(1, 99)
guess = 0
tries = 0
print "猜一个随机数"
print "你有6次机会猜中，慢慢试试"

while tries < 6 and guess != secret :
    guess = input("请输入你猜的数字： ")
    if guess < secret :
        print "太小了，猜比这个数大一点的"
    elif guess > secret :
        print "太大了，猜小一点"

    tries =tries +1

if guess ==  secret:
    print "恭喜你，猜对了"
else:
    print "没有机会了，下次再猜"
    print "随机数是：", secret





