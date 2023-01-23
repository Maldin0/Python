'''PSCP Program'''


def main():
    '''Point Sorting'''
    for _ in range(int(input())):
        data_store = []
        for _ in range(int(input())):
            temp_func = input()
            temp_dict = {}
            temp_dict['X'] = int(temp_func.split()[0])
            temp_dict['Y'] = int(temp_func.split()[1])
            temp_dict['SUM'] = sum([int(i) for i in temp_func.split()])
            data_store.append(temp_dict)
        for i in sorted(sorted(data_store, key=lambda x: x['Y'], reverse=True), key=lambda y: y['SUM']):
            print(i['X'], i['Y'])


main()
