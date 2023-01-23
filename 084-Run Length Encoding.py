'''IDK what is this'''
from itertools import groupby
def main():
    '''don't ask me bro i don't know either'''
    text = [list(g) for _, g in groupby(input())]
    for i in text:
        newi = list(i)
        print("%d%s" %(len(i), newi[0]), end='')
main()
