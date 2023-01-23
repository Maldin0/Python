'''all I want for christmas is u'''
def krisma():
    '''I don't want a lot for Christmas
There is just one thing I need
I don't care about the presents
Underneath the Christmas tree
I just want you for my own
More than you could ever know
Make my wish come true
All I want for Christmas is you, yeah'''
    width = int(input())
    tre = int(input())
    wide = 1
    for _ in range(width):
        print(("*"*wide).center(width*2))
        wide += 2
    for _ in range(tre):
        print("---".center(width*2))
krisma()
