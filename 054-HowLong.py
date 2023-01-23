'''How long'''
def howlong(num):
    '''Deez nut'''
    if num//10 == 0:
        return 1
    return 1 + howlong(num//10)
print(howlong(int(input().replace('-', ''))))
