'''Harshad'''


def harshad():
    '''HUh'''
    for _ in range(10):
        num = input()
        div = 0
        nnum = num.replace('-', '')
        for i in nnum:
            div += int(i)
        if div == 0:
            res = 'No'
        elif not float(num) % div:
            res = 'Yes'
        else:
            res = 'No'
        print(res)


harshad()
