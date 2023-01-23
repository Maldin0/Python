'''Diginiy'''


def decode():
    '''agent47'''
    while True:
        num = input()
        if num == '0':
            break
        elif len(num) == 1:
            print(num)
        else:
            print(one(num))


def one(num):
    '''Hehehuhhehahue'''
    result = 0
    if len(str(num)) == 1:
        return num
    else:
        for i in num:
            result += int(i)
        return one(str(result))


decode()
