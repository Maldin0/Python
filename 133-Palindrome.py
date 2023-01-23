'''what is this'''


def main(times, wk_t):
    '''damn he's good'''
    for _ in range(times):
        if len(wk_t) == 3:
            wk_t = three_digit_time(wk_t)

        elif len(wk_t) == 4:
            wk_t = four_digit_time(wk_t)

        print(wk_t[0] + ':' + wk_t[1:] if len(wk_t)
              == 3 else wk_t[:2] + ':' + wk_t[2:])


def four_digit_time(wk_t):
    '''Calculate the next 4-digits palindrome'''
    firsttwo, lasttwo = wk_t[:2][::-1], wk_t[2:]
    if firsttwo == lasttwo:
        wk_t = str(int(wk_t[:2])+1) + str(int(wk_t[:2])+1)[::-1]
    else:
        if int(firsttwo) > int(lasttwo):
            wk_t = wk_t[:2] + wk_t[:2][::-1]
        else:
            wk_t = str(int(wk_t[:2])+1) + str(int(wk_t[:2])+1)[::-1]
    cond = int(wk_t[:2]) > 15 and int(wk_t[:2]) < 20
    return '000' if int(wk_t[:2]) > 23 else '2002' if cond else wk_t


def three_digit_time(wk_t):
    '''Calculate the next 3-digits (or 4 when under transitional condition) palindrome'''
    firsttwo, lasttwo = wk_t[:2][::-1], wk_t[1:]
    if firsttwo == lasttwo:
        if int(str(int(wk_t[1])+1) + wk_t[2]) > 59:
            if int(str(int(wk_t[0])+1)) > 9:
                wk_t = str(int(wk_t[0])+1) + str(int(wk_t[0])+1)[::-1]
            else:
                wk_t = str(int(wk_t[0])+1) + '0' + str(int(wk_t[0])+1)
        else:
            wk_t = wk_t[0] + str(int(wk_t[1])+1) + wk_t[0]
    else:
        if int(wk_t[2]) < int(wk_t[0]):
            wk_t = wk_t[0] + wk_t[1] + wk_t[0]
        elif int(str(int(wk_t[1])+1) + wk_t[2]) > 59:
            wk_t = str(int(wk_t[0])+1) + '0' + str(int(wk_t[0])+1)
        else:
            wk_t = wk_t[0] + str(int(wk_t[1])+1) + wk_t[0]
    return wk_t


main(int(input()), input().replace(":", ""))
