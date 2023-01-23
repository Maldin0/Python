'''Blackjack'''


def blackjack(cards):
    '''21?'''
    listcards = []
    point = 0
    ace = 0
    for _ in range(cards):
        listcards.append(input())
    for i in listcards:
        if i.isnumeric():
            point += int(i)
        elif i == "J" or i == "K" or i == "Q":
            point += 10
        elif i == "A":
            point += 11
            ace += 1
    while point > 21 and ace > 0:
        point -= 10
        ace -= 1
    print(point)


blackjack(int(input()))
