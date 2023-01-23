'''PSCP Program'''


def main(txt):
    '''BreachTheDoor'''
    for i in ''.join(list(filter(lambda x: bool(x.isalpha() or x == ' '), txt))).split():
        if len(i) > 6:
            print(i, end=' ')


main(input())
