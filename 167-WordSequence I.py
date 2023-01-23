'''PSCP Program'''


def main(word):
    '''WordSequence I'''
    for i in range(1, len(word)+1):
        print(word[0:i])


main(input())
