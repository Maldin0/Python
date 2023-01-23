'''PSCP Program'''


def main(set_i, set_ii):
    '''Difference'''
    num_i, num_ii = set(), set()
    for _ in range(set_i):
        num_i.add(int(input()))
    for _ in range(set_ii):
        num_ii.add(int(input()))
    diff = sorted(num_i - num_ii)

    print(*diff)


main(int(input()), int(input()))
