'''diamond'''


def diamond(size):
    '''Diamonds Uwooooo'''
    for i in range((size//2), 0, -1):
        for _ in range(i):
            print(' ', end="")
        print('*', end="")
        for j in range(0, size-(i*2), 2):
            temp = j
        print(' '*(temp-1), end="")
        if i != size//2:
            print('*')
        else:
            print()
    print('*'*size)
    for i in range(1, (size//2)+1):
        for _ in range(i):
            print(' ', end="")
        print('*', end="")
        for j in range(0, size-(i*2), 2):
            temp = j
        print(' '*(temp-1), end="")
        if i != size//2:
            print('*')


diamond(int(input()))
