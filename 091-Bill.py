'''Bill ma boy'''
def main(cost):
    '''Bill'''
    serc = cost*(10/100)
    if serc < 50:
        serc = 50
    elif serc > 1000:
        serc = 1000
    total = serc + cost
    vat = total*(7/100)
    print("%.02f" %(total+vat))
main(int(input()))
