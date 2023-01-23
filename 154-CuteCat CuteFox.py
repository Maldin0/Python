'''PSCP Program'''
def main(times, a_cat, a_fox, count, data_list):
    '''8296-CuteCat CuteFox 15/10/2022'''
    for _ in range(times):
        temp_in = input()
        spl_d, spl_s = temp_in.split('"'), temp_in.split("'")
        temp = [spl_d[1], spl_d[3]] if len(spl_d) > len(spl_s) else [spl_s[1], spl_s[3]]
        data_list.append({'N': temp[0], 'T': temp[1][:3], 'O': int(temp[1][3:])})
    for i in data_list:
        a_cat = False if i['N'] == 'Garfield' or (i['T'] == 'Cat' and i['O'] == 1) else a_cat
        a_fox = False if i['N'] == 'Fubuki' or (i['T'] == 'Fox' and i['O'] == 1) else a_fox
        count[0] += 1 if i['T'] == 'Cat' else 0
        count[1] += 1 if i['T'] == 'Fox' else 0
    if a_cat:
        data_list.append({'N': 'Garfield', 'T': 'Cat', 'O': 1})
        count[0] += 1
    if a_fox:
        data_list.append({'N': 'Fubuki', 'T': 'Fox', 'O': 1})
        count[1] += 1
    print('Cat : %d\nFox : %d' % (count[0], count[1]))
    for i in sorted(data_list, key=lambda x: (x['T'], x['O'])):
        print("%s : %s%02d" % (i['N'], i['T'], i['O']))
main(int(input()), True, True, [0, 0], [])
