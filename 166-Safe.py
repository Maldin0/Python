'''PSCP Program'''


def main(key, passwd, tries, alp_lst):
    '''8330-Safe 14/10/2022'''
    for val1, val2 in zip(key, passwd):
        if val1 != val2:
            tries += min(abs(alp_lst.find(val1, 26, 52) - alp_lst.find(val2, 00, 26)),
                         abs(alp_lst.find(val1, 26, 52) -
                             alp_lst.find(val2, 26, 52)),
                         abs(alp_lst.find(val1, 00, 26) - alp_lst.find(val2, 26, 52)))
    print(tries)


main(input(), input(), 0, 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
