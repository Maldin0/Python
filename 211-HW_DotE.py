'''PSCP Program'''
from math import factorial as fac
def main(plyrs):
    '''8388-HW_DotE 28/10/2022'''
    plyrs += 1 if plyrs % 2 != 0 else 0
    print("%d" % ((fac(plyrs)) / ((fac(plyrs-(plyrs//2))) * (fac(plyrs//2)))))


main(int(input()))
