import random
def roll():
#随机三个数字相加，用户猜大小
    times=3
    points = []
    print('<<<<< GAME STARTS! >>>>>')
    user_point=input('Big or Small:')
    print('<<<<< ROLE THE DICE! >>>>>')
    while times>0:
        point=random.randrange(1,7)
        points.append(point)
        times=times-1
    total=sum(points)
    isBig=11<=total<=18
    isSmall=3<=total<=10
    if (isBig and user_point=='Big') or (isSmall and user_point=='Small'):
        print(points,'You Win!')
        roll()
    else:
        print(points,'You Lose!')
        roll()
roll()

