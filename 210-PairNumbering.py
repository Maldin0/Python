'''PSCP Program'''
def main():
    '''8387-PairNumbering 06/11/2022'''
    count = 0
    lst1, lst2, pair = listify(input()), listify(input()), int(input())
    lst1 = [i for i in lst1 if i <= pair]
    for i in set(lst1):
        matched = lst2.count(pair - i)
        if matched >= 1:
            count += lst1.count(i) * matched
    print(count)

def listify(lst):
    '''Convert str to list'''
    return [int(i) for i in lst.replace('[', '').replace(']', '').split(', ')]
main()
