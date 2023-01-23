'''Calculator'''


def cal(num, tempi):
    '''Henlo'''
    if num == 1:
        res = 1
    else:
        for i in range(1, num+1):
            tempi += str(i)+'+'
        res = len(tempi)
    print(res)


cal(int(input()), '')
