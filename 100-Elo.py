'''Elo'''


def elo(raa, rbb, team):
    '''Hardstuck Gold IV'''
    if team == 'A':
        result = "%.02f" % (1/(1+(10**((rbb-raa)/400))))
    elif team == 'B':
        result = "%.02f" % (1/(1+(10**((raa-rbb)/400))))
    print(result)


elo(int(input()), int(input()), input())
