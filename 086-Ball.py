'''Ligma balls'''
def ball(bounce):
    '''hehe'''
    num = 0
    while bounce >= 0.01:
        bounce *= 3/5
        if  bounce >= 0.01:
            num += 1
    print(num)
ball(float(input()))
