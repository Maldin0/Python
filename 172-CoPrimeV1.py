'''PSCP Program'''


def main(num_1, num_2, num):
    '''CoPrime_v1'''
    for i in range(1, max(num_1, num_2)+1):
        if num_1 % i == 0 and num_2 % i == 0:
            num.append(i)
    print('YES\n1' if len(num) == 1 else 'NO\n%d' % max(num))


main(int(input()), int(input()), [])
