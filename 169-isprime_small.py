'''PSCP Program'''


def main(number):
    '''isprime_small'''
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print('No')
                break
        else:
            print('Yes')
    else:
        print('No')


main(int(input()))
