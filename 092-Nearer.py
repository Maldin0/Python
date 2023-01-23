'''Nearer'''
def nearer(alice, bob, icecream):
    '''Huehuhehehehuh'''
    if abs(alice-icecream) > abs(bob-icecream):
        text = "Bob %d" %(abs(bob-icecream))
    elif abs(alice-icecream) < abs(bob-icecream):
        text = "Alice %d" %(abs(alice-icecream))
    else:
        text = "Sundaes %d" %(abs(alice-icecream))
    print(text)
nearer(int(input()), int(input()), int(input()))
