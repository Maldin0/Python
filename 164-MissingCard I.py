'''PSCP Program'''


def main(card, my_card, list1):
    '''MissingCard I'''
    for i in 'SHDC':
        for j in list1:
            card.add(j+i)
    for _ in range(51):
        my_card.add(input())
    print(*(card - my_card))


main(set(), set(), ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'])
