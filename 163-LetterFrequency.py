'''PSCP Program'''


def main(text, stats):
    '''LetterFrequency'''
    for i in text:
        stats[i] = 0
    for i in text:
        stats[i] += 1
    for i in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        if i[0].isalpha():
            print(i[0])
            break


main(input().lower().replace(' ', ''), {})
