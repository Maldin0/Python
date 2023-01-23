'''PSCP Program'''
def main(data, temp, data_lst):
    '''8343-Flatten 21/10/2022'''
    for i in data[1:-1] + ' ':
        if i.isnumeric() or i == '-':
            temp += i
        elif len(temp):
            data_lst.append(int(temp))
            temp = ''
    print(sorted(data_lst, reverse=True))
main(input(), '', [])
