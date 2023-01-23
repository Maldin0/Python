'''PSCP Program'''


def main(group_i, group_ii):
    '''Duplicate I'''
    grp_i, grp_ii = [], []
    for _ in range(group_i):
        grp_i.append(input())
    for _ in range(group_ii):
        grp_ii.append(input())
    diff = sorted(set(grp_i) & set(grp_ii), reverse=True)
    if len(diff) == 0:
        print('Nope')
    else:
        print(*diff, sep='\n')


main(int(input()), int(input()))
