'''Donut'''
def main(numa, numb, numc, numd):
    """main"""
    sumpro = numb+numc
    numcount = numd//sumpro
    numdif = numd-sumpro*numcount
    if numdif >= numb:
        numcount += 1
        cost = numcount*numb*numa
        receive = sumpro*numcount
    else:
        cost = (numcount*numb + numdif)*numa
        receive = numcount*sumpro+numdif
    print(cost, receive)
main(int(input()), int(input()), int(input()), int(input()))
