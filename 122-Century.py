'''hehe'''


def main():
    '''Century'''
    for _ in range(int(input())):
        text = input()
        if text[:4] == 'B.E.' and int(text[5:])-543 >= 0:
            print(-((int(text[5:])-543)//-100))
        elif text[:4] == 'A.D.' and int(text[5:]) >= 0:
            print((-(int(text[5:])//-100)))
        else:
            print('ERROR')


main()
