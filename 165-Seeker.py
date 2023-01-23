'''PSCP Program'''


def main(buffer):
    '''8329-Seeker 14/10/2022'''
    for i in input():
        buffer += i if i.isnumeric() else ' '
    print(sum(map(int, buffer.split())))


main('')
