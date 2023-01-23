'''Heh'''


def coke(price, caps, promo, wanted):
    '''Damn I try undeleting my own code at a10 in l207 sadly i can't bring it back so this'll do'''
    valid, buying, paying_price, first_run = False if caps == 0 else True, 0, 0, True
    while buying < wanted:
        if price == 0 or wanted == 0:
            break
        cond1, cond2 = buying < wanted, promo < price
        if caps == 0 and not valid:
            cond3 = True
        else:
            cond3 = buying % caps != 0
        if valid and cond1 and cond2 and buying % caps == 0 and buying > 0:
            paying_price += promo
            buying += 1
        if (not (promo == 0 and caps == 1) and buying < wanted and cond3) or first_run:
            first_run = False
            buying += 1
            paying_price += price

    print(paying_price)


coke(int(input()), int(input()), int(input()), int(input()))
