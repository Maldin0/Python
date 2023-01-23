'''PSCP Program'''


def main(num_1, num_2):
    '''GCD_v1'''
    num = []
    for i in range(1, max(num_1, num_2)+1):
        if num_1 % i == 0 and num_2 % i == 0:
            num.append(i)
    print(max(num))


main(int(input()), int(input()))
