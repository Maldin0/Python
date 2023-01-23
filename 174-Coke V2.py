'''PSCP Program'''


def main(price, caps, promo, wanted):
    '''8340-Coke V2 15/10/2022'''
    if caps > 0 and wanted > 0 and price > 0:
        wanted -= 1
        print(((wanted // caps) * ((price*(caps-1))+promo)) +
              ((wanted % caps) * price) + price)
    else:
        print(wanted * price)


main(int(input()), int(input()), int(input()), int(input()))
