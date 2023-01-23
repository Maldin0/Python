'''oh yeah'''


def main():
    '''dang he's too good'''
    mob_c, bsc_c, std_c, prm_c, scr, pho = 0, 0, 0, 0, int(
        input()), int(input())
    _, _ = input(), input()
    on_tv, hd1080, uhd4k = input() == 'Yes', input() == 'Yes', input() == 'Yes'
    calc_t = pho if pho >= scr else scr
    while calc_t > 0:
        if not (on_tv or hd1080 or uhd4k):
            mob_c += calc_t
            calc_t -= calc_t
        elif not (hd1080 or uhd4k):
            if calc_t >= 4:
                prm_c += calc_t // 4
                calc_t -= (calc_t // 4) * 4
            elif calc_t >= 3:
                prm_c += -(calc_t // -4)
                calc_t -= -(calc_t // -4) * 4
            elif calc_t >= 2:
                std_c += -(calc_t // -2)
                calc_t -= -(calc_t // -2) * 2
            else:
                bsc_c += calc_t
                calc_t -= calc_t
        elif not uhd4k:
            if calc_t >= 4:
                prm_c += calc_t // 4
                calc_t -= (calc_t // 4) * 4
            elif calc_t >= 3:
                prm_c += -(calc_t // -4)
                calc_t -= -(calc_t // -4) * 4
            else:
                std_c += -(calc_t // -2)
                calc_t -= -(calc_t // -2) * 2
        elif uhd4k:
            prm_c += -(calc_t // -4)
            calc_t -= -(calc_t // -4) * 4
    report(prm_c, std_c, bsc_c, mob_c)


def report(prm_c, std_c, bsc_c, mob_c):
    '''Prints output'''
    if prm_c > 0:
        print('Premium x %d' % prm_c)
    if std_c > 0:
        print('Standard x %d' % std_c)
    if bsc_c > 0:
        print('Basic x %d' % bsc_c)
    if mob_c > 0:
        print('Mobile x %d' % mob_c)
    print('Total = %d THB' %
          ((prm_c*419) + (std_c*349)+(bsc_c*279) + (mob_c*99)))


main()
