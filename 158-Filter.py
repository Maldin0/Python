'''Filter'''


def main(data_stats, minimum, data_list, flag):
    '''Filter'''
    data_stats = data_stats.replace('{', '').replace('}', '').split(', ')
    for i in data_stats:
        i = i.replace('"', '').split(': ')
        temp_dict = {}
        temp_dict['ID'] = i[0]
        temp_dict['Score'] = float(i[1])
        data_list.append(temp_dict)
    for i in sorted(data_list, key=lambda x: x['ID']):
        if i['Score'] >= minimum:
            print("%s\t%.02f" % (i['ID'], i['Score']))
            flag = False
    if flag:
        print('Nope')


main(input(), float(input()), [], True)
