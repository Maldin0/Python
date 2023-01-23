'''Pringles'''


def pringles(can1, can2, can3, reach,):
    '''Pringles'''
    unreachable = 0
    reachable = 0
    start = None
    dark_space = 0
    for i, j in enumerate(can2):
        if i >= len(can1) - (len(can1) - reach):
            if j == ')':
                unreachable += 1
                dark_space += 1
            elif j == ' ':
                dark_space += 1
            if start is None:
                start = i
        elif j == ')':
            reachable += 1
    print(reachable)
    if unreachable == 0:
        print('None.')
        start = 0
    else:
        print('There are still some left.')
    print(can1)
    if unreachable == 0:
        print(' '*len(can1) + '|')
    else:
        print(' '*(len(can1) - dark_space) + can2[start:])
    print(can3)


pringles(input(), input(), input(), int(input()))
