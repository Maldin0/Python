'''PSCP Program'''
from collections import Counter as cout
def main():
    '''8424-Difference 06/11/2022'''
    lst1, lst2 = listify(input()), listify(input())
    tmp = cout(lst1)
    tmp.subtract(cout(lst2))
    out_lst = [{'L': i, 'V': abs(j)} for i, j in {i:j for i, j in tmp.items() if j != 0}.items()]
    if len(out_lst) == 0:
        print('ONAJI DAYO!')
    else:
        for i in sorted(out_lst, key=lambda x: x['L']):
            print(i['L'], i['V'])
def listify(lst):
    '''Convert str list to list'''
    temp, out_temp, flag = '', [], False
    for i in lst:
        if i in ('"', "'"):
            if flag:
                out_temp.append(temp)
                temp = ''
            flag = not flag
            continue
        if flag:
            temp += i
    return out_temp
main()
