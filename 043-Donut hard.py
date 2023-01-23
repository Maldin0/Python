'''Donut'''
def donut():
    '''Cops only takes donut as a bribe'''
    cost = int(input())
    buy = int(input())
    free = int(input())
    want = int(input())
    take = 0
    amount = 0
    count = 0
    if want > buy:
        if want%buy == 0:
            count = want//buy-1
            if count == 0:
                count = 1
            for _ in range(count):
                take += free
        else:
            count = want//buy
            for _ in range(count):
                take += free
    elif want == buy:
        count = want//buy
        take += free
    amount = count*buy
    lastamo = amount
    amount += take
    total = 0
    while amount < want:
        total += cost
        amount += 1
    total += lastamo*cost
    print("%d %d" %(total, amount))
donut()
