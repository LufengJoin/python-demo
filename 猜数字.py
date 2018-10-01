import random
secret=random.randint(1,20)
print('-----------猜数字----------')
temp=input("不妨猜一下我心中想的数字是多少：")
guess=int(temp)
while guess!=secret:
    temp=input("猜错了，请再猜一次吧：")
    guess=int(temp)
    if guess==secret:
        print("恭喜你，猜对啦")
    else:
        if guess>secret:
            print("哥，大了大了")
        else:
            print("嘿，小了小了")
print("游戏结束，不玩啦*╹▽╹*")
