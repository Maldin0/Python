'''PSCP Program'''


def main():
    '''PickThemAgain'''
    data = [int(i) for i in input().split()]
    out = []
    for i in reversed(data):
        if i % 3 == 0 or i % 5 == 0:
            out.append(i)
    if len(out) == 0:
        print('Nope')
    else:
        print(*out, sep='\n')


main()
