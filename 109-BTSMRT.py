'''BTSMRT'''


def btsmrt(day, ages, height):
    '''HUh'''
    if ages < 14 and height < 90:
        result = 'FREE'
    elif ages < 14 and height <= 140 and day == 'Children Day':
        result = 'FREE'
    elif ages >= 60 and day == 'Senior Day':
        result = 'FREE'
    else:
        result = 'PAY'
    print(result)


btsmrt(input(), float(input()), float(input()))
