'''PSCP Program'''
def main(total_dist, participants):
    '''Runner'''
    stor = []
    for i in range(1, participants+1):
        runner = [int(i) for i in input().split()]
        data_dict = {}
        data_dict['i'] = i
        data_dict['s'] = runner[0]
        data_dict['t'] = (total_dist - runner[1]) / runner[0]
        stor.append(data_dict)
    for i in sorted(sorted(stor, key=lambda x: x['s'], reverse=True), key=lambda x: x['t']):
        print(i['i'])
        break

main(int(input()), int(input()))
