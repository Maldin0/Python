'''Classy'''


def main(data_list, track, prev):
    '''Uwooooo seqqq'''
    while True:
        data = input()
        if data == 'END':
            break
        data_list.append({'Year': int(data[:2]), 'Faculty': int(data[2:4])})
        track.append(data[:2] + str(int(data[2:4])))

    data_list.sort(key=lambda x: (x['Year'], x['Faculty']))
    data_list = [i for n, i in enumerate(
        data_list) if i not in data_list[n + 1:]]

    for i, j in enumerate(data_list):
        data_list[i]['Count'] = track.count(str(j['Year'])+str(j['Faculty']))

    for i in data_list:
        if prev is None:
            prev = i['Year']
            print(i['Year'], i['Faculty'], i['Count'])
            continue
        if prev == i['Year']:
            print('--', i['Faculty'], i['Count'])
        else:
            print(i['Year'], i['Faculty'], i['Count'])
        prev = i['Year']


main([], [], None)
