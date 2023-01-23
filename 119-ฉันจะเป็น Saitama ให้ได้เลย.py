'''Huhuh'''


def main():
    '''Saitama'''
    push_up, sit_up, stand_sit, run = int(input()), int(
        input()), int(input()), int(input())
    r_push_up, r_sit_up, r_run, r_stand_sit = int(
        input()), int(input()), int(input()), int(input())
    day_1 = -(push_up // -r_push_up)
    day_2 = -(sit_up // -r_sit_up)
    day_3 = -(stand_sit // -r_stand_sit)
    day_4 = -(run // -r_run)
    print(reorder_num(day_1, day_2, day_3, day_4))


def reorder_num(num_a, num_b, num_c, num_d):
    '''Reorder given number to ascending tuple'''
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
    return str(num_d)


main()
