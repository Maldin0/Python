'''amogus'''


def main():
    '''sugoma'''
    dic = {}
    ded = []
    ded_crew = []
    alive_crew = []
    sussy = 0
    while True:
        dict_in = input()
        if dict_in[:2] == '{"':
            temp = dict_in.replace('"}', '').replace('{"', '').split('" : "')
            dic[temp[0]] = temp[1]
        if dict_in == 'Start':
            break
    while True:
        vote = input()
        if vote == 'End':
            break
        ded.append(vote)
    for i, j in sorted(dic.items()):
        if i in ded:
            ded_crew.append({i: j})
        else:
            if j == 'Impostor':
                sussy += 1
            alive_crew.append({i: j})
    res(sussy, alive_crew, ded_crew)


def res(sussy, alive_crew, ded_crew):
    '''heheboi'''
    print('%d Impostor Remains' % sussy)
    print('***Alive***')
    for i in alive_crew:
        for j, k in i.items():
            print(j, k, sep=' : ')
    print('***Dead***')
    for i in ded_crew:
        for j, k in i.items():
            print(j, k, sep=' : ')


main()
