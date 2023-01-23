'''Parity'''


def main(data, txt, num1):
    '''Hello'''
    for i in data:
        if i == "1":
            num1 += 1
    if txt == "Even":
        if num1 % 2 == 0:
            data += '0'
        else:
            data += '1'
    if txt == 'Odd':
        if num1 % 2 == 0:
            data += '1'
        else:
            data += '0'
    print(data)


main(input(), input(), 0)
