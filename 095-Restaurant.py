'''Restaurant'''


def main(cost, buy, promo, sugg):
    """main"""
    if cost >= buy:
        total1 = cost*((100-promo)/100)-cost
    else:
        total1 = 0
    if cost+sugg >= buy:
        total2 = (cost+sugg)*((100-promo)/100)-cost
    else:
        total2 = 0
    final = total2-total1
    if final < 0:
        worth = "Yes %.03f" % abs(final)
    elif final > 0:
        worth = "No %.03f" % final
    elif final == 0:
        worth = "Yes"
    print(worth)


main(float(input()), float(input()), float(input()), float(input()))
