'''PSCP Program'''


def main():
    '''Missing Number'''
    data = []
    missing = []
    highest = int(input())
    while True:
        num = int(input())
        if num == 0:
            break
        data.append(num)
    for i in range(1, highest+1):
        if i not in data:
            missing.append(i)

    print(*missing, sep='\n')


main()
