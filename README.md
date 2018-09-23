# python-demo
practice
print('--------------猜数字-----------')
temp=input("猜猜我心里想的数字是什么：")
guess=int(temp)
if guess==66:
    print("好厉害!")
    print("哼！不过猜中也没奖励")
else:
    if guess<66:
        print("猜小啦！笨蛋")
    else:
        print("猜大啦！笨蛋")
    print("游戏结束")
