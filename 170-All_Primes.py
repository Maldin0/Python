'''PSCP Program'''


def main(number, count):
    '''All_Primes'''
    if number == 2:
        count += 1
    for j in range(1, number+1):
        if j > 1:
            for i in range(2, j):
                if (j % i) == 0:
                    break
            else:
                count += 1
    print(count)


main(int(input()), 0)
