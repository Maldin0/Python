'''PSCP Program'''


def main(word1, word2):
    '''WordSequence II'''
    length = max(len(word1), len(word2))
    for i in range(length+1):
        out = word2[:i] + word1[i:]
        print(out)


main(input(), input())
