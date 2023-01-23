'''PSCP Program'''
def main(isbn):
    '''8431-ISBN 05/11/2022'''
    data, check, temp, out = list(isbn[:-1]), isbn[-1], 10, 0
    for i in data:
        out += int(i) * temp
        temp -= 1
    check_digits = (-out) % 11
    check_digits = 'X' if len(str(check_digits)) == 2 else str(check_digits)
    print('Yes' if check_digits == check else 'No %s' % check_digits)
main(input().replace('-', ''))
