'''PSCP Program'''


def main():
    '''PickThem'''
    data = [int(i) for i in input().replace('[', '').replace(']', '').split(', ')]
    out = []
    for i in data:
        if i % 2 == 0:
            out.append(i)
    if len(out) == 0:
        print('Nope')
    else:
        print(*out, sep='\n')


main()
