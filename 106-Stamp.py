'''Stamps'''


def stamps(times, every, get, num, free):
    '''huh'''
    res = 0
    stamp = 0
    for _ in range(times):
        totalprice = int(input())
        while stamp >= num and totalprice > 0:
            totalprice -= free
            stamp -= num
            if totalprice < 0:
                totalprice = 0
        res += totalprice
        stamp += (totalprice//every)*get
    print(res, stamp, sep="\n")


stamps(int(input()), int(input()), int(input()), int(input()), int(input()))
