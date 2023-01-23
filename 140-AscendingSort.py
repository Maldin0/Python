'''PSCP Program'''


def main():
    '''AscendingSort'''
    data = []
    for _ in range(5):
        data.append(int(input()))
    print(*sorted(data), sep='\n')


main()
