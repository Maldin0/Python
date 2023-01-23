'''One for all'''


def main(number):
    '''One For All'''
    out = ''
    for i in range(number):
        if i+1 == number:
            ending = '_' + str(number)
        elif (i+1) % 2 == 1:
            ending = '*'*(i+1)
        else:
            ending = '-'*(i+1)
        out += input() + ending
    print(out)


main(int(input()))
