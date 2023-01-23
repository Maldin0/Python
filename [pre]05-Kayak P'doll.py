"""[Pre] Kayak"""
def main():
    """main"""
    allnum = int(input())
    num = input().split(" ")
    weight = []
    for i in range(allnum*2):
        weight += [int(num[i])]
    weight.sort()
    lastans = 0
    while weight != []:
        for k in range(len(weight)-1):
            if k == 0:
                dif = weight[k+1]-weight[k]
                newdif = dif+1
                numx = k
            else:
                newdif = weight[k+1]-weight[k]
            if dif < newdif:
                dif = dif
            elif dif > newdif:
                dif = newdif
                numx = k
        lastans += dif
        weight.pop(int(numx))
        weight.pop(int(numx))
    lastans -= dif
    print(lastans)
main()
