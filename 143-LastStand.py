'''PSCP Program'''


def main():
    '''LastStand'''
    data = [int(i) for i in input().replace(
        '[', '').replace(']', '').split(',')]
    print(data)
    for i in data:
        print(str(i)[-1])


main()
