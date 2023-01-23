'''PSCP Program'''
def main():
    '''Diamond I'''
    var_m, var_n = int(input()), int(input())
    loc_store = []
    data_dict = {}
    out = []
    for _ in range(var_m):
        data = [int(i) for i in input().split()]
        loc_store.append(data)
    for i in range(1, var_n+1):
        data_dict[i] = 0
    for i in range(var_m):
        for j in range(1, var_n+1):
            data_dict[j] += loc_store[i][j-1]
    for i in sorted(data_dict, key=data_dict.get, reverse=True):
        out.append(data_dict[i])
    print(max(out))
main()
