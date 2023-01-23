'''Henlo'''


def tugowar():
    '''Squid Game 3 - Tug-of-War'''
    team_a, team_b = 0, 0
    for _ in range(10):
        team_a += int(input())
    for _ in range(10):
        team_b += int(input())
    if team_a > team_b:
        print('B')
    elif team_a < team_b:
        print('A')
    else:
        print('AB')


tugowar()
