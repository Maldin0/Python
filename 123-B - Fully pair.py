'''Shall we dance?'''


def main():
    '''B - Fully pair?'''
    pair, temp, data_dict = input(), '', {}
    for j in pair:
        data_dict[j] = 0
    for j in pair:
        data_dict[j] += 1
    for i, j in data_dict.items():
        if j % 2 != 0:
            temp += i
    if temp == '':
        print('fully paired')
    else:
        print(temp)


main()
