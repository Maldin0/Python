'''PSCP Program'''
def main(money, interest, years):
    '''8399-Compound Interest 28/10/2022'''
    for _ in range(years):
        money = money + (money*(interest/100))
    print("%.02f"%money)

main(int(input()), float(input()), int(input()))
