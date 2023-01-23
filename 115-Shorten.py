'''Shorten'''


def shorten():
    '''Shorten'''
    out, prev, plus_count, first_run = '', 0, 1, True
    while True:
        num = int(input())
        if num == -1:
            if first_run:
                print()
            else:
                out += str(prev + plus_count - 1)
            break
        if first_run:
            first_run, prev = False, num
        else:
            if prev + plus_count == num:
                if plus_count == 1:
                    out += str(prev) + '-'
                plus_count += 1
            else:
                out += str(prev + plus_count - 1) + ', '
                prev, plus_count = num, 1
    print(out)


shorten()
