'''Winner take all'''
def rps(get):
    '''Yeah baby'''
    listget = [get[i:i+2] for i in range(0, len(get), 2)]
    rscount = listget.count('RS') #Awin
    prcount = listget.count('PR') #Awin
    spcount = listget.count('SP') #Awin
    rpcount = listget.count('RP') #Bwin
    pscount = listget.count('PS') #Bwin
    srcount = listget.count('SR') #Bwin
    apoint = rscount+prcount+spcount
    bpoint = rpcount+pscount+srcount
    if apoint == bpoint:
        result = "DRAW %d" %apoint
    elif apoint > bpoint:
        result = "A win %d-%d" %(apoint, bpoint)
    elif apoint < bpoint:
        result = "B win %d-%d" %(bpoint, apoint)
    print(result)
rps(input())
