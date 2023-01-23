'''PSCP Program'''
def main():
    '''8378-CoinChangev1 28/10/2022'''
    given = int(input())
    coin_25 = given // 25
    given -= (given // 25) * 25
    coin_10 = given // 10
    given -= (given // 10) * 10
    coin_5 = given // 5
    given -= (given // 5) * 5

    print(coin_25+coin_10+coin_5+given)


main()
