'''hehe'''
def seq(ran):
    '''HeHehaha'''
    num = []
    for i in range(ran):
        num.append(i+1)
    print(*num, sep=" ")
    for j in range(ran-1):
        new_num = [k+(j+1)*ran for k in num]
        print(*new_num, sep=" ")
seq(int(input()))
