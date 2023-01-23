'''OMg'''


def main(text, stats):
    '''man im dead'''
    for i in text:
        stats[i] = 0
    for i in text:
        stats[i] += 1
    for i in sorted(stats, key=str.swapcase):
        print(i, graph(stats[i]), sep=' : ')


def graph(num, out=''):
    '''Add | to historgram'''
    for i in range(1, num+1):
        if (i-1) % 5 == 0 and i > 4:
            out += '|-'
        else:
            out += '-'
    return out


main(input(), {})
