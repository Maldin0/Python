'''Key'''
def key():
    '''OMG'''
    idnum = input()
    listidnum = [int(i) for i in idnum]
    sumidnum = sum(listidnum)
    last3dig = (int(idnum)%1000)*10
    keys = sumidnum+last3dig
    if len(str(keys)) > 4:
        keys %= 1000
    elif len(str(keys)) < 4:
        keys += 1000
    print("%04d" %keys)
key()
