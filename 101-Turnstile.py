'''Turnstile'''


def turnstile():
    '''I ain't got any money bro'''
    lock = True
    count = 0
    coin = ''
    while coin != 'END':
        coin = input()
        if coin == 'C' and lock:
            lock = False
        if coin == 'P' and not lock:
            count += 1
            lock = True
    print(count)


turnstile()
