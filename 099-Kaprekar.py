'''Kaprekar'''


def reorder(num):
    '''reorder Cr. jarukit'''
    num_a, num_b, num_c, num_d = int(num[0]), int(
        num[1]), int(num[2]), int(num[3])
    if num_a > num_b:
        num_a, num_b = num_b, num_a
    if num_c > num_d:
        num_c, num_d = num_d, num_c
    if num_a > num_c:
        num_a, num_c = num_c, num_a
    if num_b > num_d:
        num_b, num_d = num_d, num_b
    if num_b > num_c:
        num_b, num_c = num_c, num_b
    return str(num_a), str(num_b), str(num_c), str(num_d)


def kaprekar(num):
    '''More like paprika'''
    count = 0
    result = 0
    nnum = reorder(num)
    while result != 6174:
        lowest = int(nnum[0]+nnum[1]+nnum[2]+nnum[3])
        highest = int(nnum[3]+nnum[2]+nnum[1]+nnum[0])
        result = highest-lowest
        nnum = reorder(str(result).zfill(4))
        count += 1
    print(count)


kaprekar(input())
