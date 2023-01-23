'''Lotto'''


def lotto():
    '''Wooooo yeah baby that's what i've waiting for that's what it's all about'''
    first = input()
    last2 = input()
    first3d1, first3d2 = input(), input()
    last3d1, last3d2 = input(), input()
    mine = input()
    win = 0
    if first == '999999':
        nearfirst = '000000', '999998'
    elif first == '000000':
        nearfirst = '000001', '999999'
    else:
        nearfirst = str(int(first)+1).zfill(6), str(int(first)-1).zfill(6)
    if mine == first:
        win += 6000000
    if mine in nearfirst:
        win += 100000
    if mine[-2:] == last2:
        win += 2000
    if mine[:3] == first3d1:
        win += 4000
    if mine[:3] == first3d2:
        win += 4000
    if mine[-3:] == last3d1:
        win += 4000
    if mine[-3:] == last3d2:
        win += 4000
    print(win)


lotto()
