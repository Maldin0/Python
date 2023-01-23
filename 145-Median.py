'''PSCP Program'''


def main():
    '''Median'''
    data = []
    for _ in range(int(input())):
        data.append(int(input()))
    data.sort()
    if len(data) % 2 == 1:
        print("%.1f" % data[int(((len(data)+1)/2)-1)])
    elif len(data) % 2 == 0:
        print("%.1f" % ((data[int((len(data)/2) - 1)] + data[int((len(data) / 2))]) / 2))


main()
 