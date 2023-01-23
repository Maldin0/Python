'''PSCP'''


def milkies(price, buy, get, got):
    '''Milk'''
    milk = got//price
    bottle = milk
    while bottle >= buy and buy != 0:
        free = (bottle // buy) * get
        milk += free
        bottle -= (bottle // buy) * buy
        bottle += free
    print(milk)


milkies(int(input()), int(input()), int(input()), int(input()))
