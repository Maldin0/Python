'''Runner'''
def rep(text, time):
    '''Repeat what i said'''
    for _ in range(time):
        print(text)
rep(input(), int(input()))
