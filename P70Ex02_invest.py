def invest(amount,rate,time):
#复利计算
    print('Principal amount:{}'.format(amount))
    print('Rate:'+str(rate))
    for i in range(1,time+1):
        amount=amount*(1+rate)
        print('year {}: ${}'.format(i,amount))

invest(100,0.05,8)

