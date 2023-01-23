'''PSCP Program'''


def main(countries, data_list, prev):
    '''Olympic'''
    for _ in range(countries):
        temp = input().split()
        data_list.append({'NAME': temp[0], 'GLD': int(temp[1]), 'SVL': int(temp[2]),
                          'BRO': int(temp[3]), 'Total': int(temp[1])+int(temp[2])+int(temp[3])})
    for i, j in enumerate(sorted(data_list, key=lambda x: (-x['GLD'], -x['SVL'], -x['BRO'],\
                          -x['Total'], x['NAME']))):
        if prev is None:
            prev = (str(j['GLD']) + str(j['SVL']) +
                    str(j['BRO']) + str(j['Total']), i+1)
            print(i+1, j['NAME'], j['GLD'], j['SVL'], j['BRO'], j['Total'])
            continue
        if prev[0] == str(j['GLD']) + str(j['SVL']) + str(j['BRO']) + str(j['Total']):
            print(prev[1], j['NAME'], j['GLD'], j['SVL'], j['BRO'], j['Total'])
            prev = (str(j['GLD']) + str(j['SVL']) +
                    str(j['BRO']) + str(j['Total']), prev[1])
        else:
            print(i+1, j['NAME'], j['GLD'], j['SVL'], j['BRO'], j['Total'])
            prev = (str(j['GLD']) + str(j['SVL']) +
                    str(j['BRO']) + str(j['Total']), i+1)


main(int(input()), [], None)
